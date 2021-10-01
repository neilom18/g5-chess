
# chat/consumers.py
import json
from main.game.especialMoves import EnPassant
from main.game.game import selectPiece
from main.game.ConvertStringArray import arrayToStringallPieces, arrayTostring, stringToArray, arrayToHistory
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Room


class RoomConsumer(WebsocketConsumer):
    def connect(self):
        #por causa do all auth já estar como padrão ao executarmos o self.scope ele já nos retorna o usuário logado
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.Room,created = Room.objects.get_or_create(roomCode=self.room_group_name)
        if created:
            self.Room.user1= str(self.scope['user'])
        else:
            if self.Room.user1 == str(self.scope['user']):
                pass
            else:
                self.Room.user2 = str(self.scope['user'])
            
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        if self.Room.user1 != '' and self.Room.user2 != '':
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type':'start_game',
                    'data':{
                        'user1':self.Room.user1,
                        'user2':self.Room.user2
                    }
                }
            )
        self.Room.save()
        self.accept()


    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['data']['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))

    def start_game(self,data):
        usuario1 = data['data']['user1']
        usuario2 = data['data']['user2']
        if usuario1 == str(self.scope['user']):
            self.send(text_data=json.dumps({
                'userColor':'w',
                'message':'game has been started you are white pieces',
                'startGame':self.Room.pieces
            }))
        elif usuario2 == str(self.scope['user']):
            self.send(text_data=json.dumps({
                'userColor':'b',
                'message':'game has been started you are black pieces',
                'startGame':self.Room.pieces
            }))

   
    def get_name(self, data):
        self.username = data['data']['username']

    def select_piece(self,data):
        #recolhe a peça que foi selecionada
        allPieces = stringToArray(self.Room.pieces)
        piece = data['data']['piece']
        color = piece[1]
        if color =='w' and self.Room.user1 == str(self.scope['user']) and self.Room.whoMove == True:
            #recolhe todas as peças no backend
            #checa se a peça existe
            for line in allPieces:
                for pieceInBack in line:
                    if pieceInBack == piece:
                        #se a peça existir vou retornar o movimentos possíveis caso haja se não apenas retorno a peça
                        moves = selectPiece(allPieces,piece,self.Room)
                        if piece == moves.strip():
                            self.send(text_data=json.dumps({
                                'message':'nenhum movimento possível',
                                'piece':piece
                            }))
                        else:
                            self.send(text_data=json.dumps({
                                'message':'moves',
                                'moves':moves.strip()
                            }))
        elif color=='b' and self.Room.user2 == str(self.scope['user']) and self.Room.whoMove == False:
             for line in allPieces:
                    for pieceInBack in line:
                        if pieceInBack == piece:
                            #se a peça existir vou retornar o movimentos possíveis caso haja se não apenas retorno a peça
                            moves = selectPiece(allPieces,piece,self.Room)
                            if piece == moves.strip():
                                self.send(text_data=json.dumps({
                                    'message':'nenhum movimento possível',
                                    'piece':piece
                                }))
                            else:
                                self.send(text_data=json.dumps({
                                    'message':'moves',
                                    'moves':moves.strip()

                                }))

    def actualizeWhoMove(self,data):
        move = data['data']['data']['move']
        move = move.split(' ')
        color = move[0][1]
        if color == 'w':
            self.Room.whoMove = False
        else:
            self.Room.whoMove = True
    #executa os movimentos para a peça selecionada
    def move_piece(self,data):
        EnPassant = False
        #actualize move for all players
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'actualizeWhoMove',
                'data':data
            }
        )
        move = data['data']['move']
        move = move.split(' ')
        pieces = self.Room.pieces
        piecesArray = stringToArray(pieces)

        #atualiza o histórico para os players
        if self.Room.history != '':
            self.Room.history = self.Room.history + arrayToHistory(move) +','
        else:
            self.Room.history = arrayToHistory(move)+','
        print(self.Room.history)
        for line in piecesArray:
            for piece in line:
                if piece == move[0]:
                    #verifica se é um peão
                    if move[0][0] == 'p':
                        #verifica se é um movimento EnPassant
                        if move[0][3] != move[1][3]:
                            if piecesArray[int(move[1][2])][int(move[1][3])] == '----':
                                #aplica o EnPassant
                                piecesArray[int(piece[2])][int(piece[3])] = '----'
                                piecesArray[int(move[1][2])][int(move[1][3])] = move[1]
                                if move[0][1] == 'w':
                                    move.append(piecesArray[int(move[1][2])-1][int(move[1][3])])
                                    piecesArray[int(move[1][2])-1][int(move[1][3])] = '----'
                                else:
                                    move.append(piecesArray[int(move[1][2])+1][int(move[1][3])])
                                    piecesArray[int(move[1][2])+1][int(move[1][3])] = '----'
                                print(move)
                                EnPassant = True
                                print(move[1])
                                self.send(text_data=json.dumps({
                                    'message':'moved',
                                    'enPassant':move
                                }))
                    if EnPassant == False:
                        piecesArray[int(piece[2])][int(piece[3])] = '----'
                        piecesArray[int(move[1][2])][int(move[1][3])] = move[1]
                        move_piece = move
                        self.send(text_data=json.dumps({
                            'message':'moved',
                            'movePiece':move_piece
                        }))
                        print(piecesArray[4][4])
                    self.Room.pieces = arrayToStringallPieces(piecesArray)


    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        command = text_data_json['command']
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':command,
                'data':text_data_json,
            }
        )