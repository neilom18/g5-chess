
# chat/consumers.py
from time import time
import json
from main.game.especialMoves import EnPassant
from main.game.game import selectPiece
from main.game.ConvertStringArray import arrayToStringallPieces, arrayTostring, stringToArray, arrayToHistory
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from main.game.verifyCheck import verificarMate
from .models import Room,GameHistory


class RoomConsumer(WebsocketConsumer):
    def connect(self):
        #por causa do all auth já estar como padrão ao executarmos o self.scope ele já nos retorna o usuário logado
        self.time = time
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
            'message': message,
            'usuario':event['usuario']
        }))

    def start_game(self,data):
        usuario1 = data['data']['user1']
        usuario2 = data['data']['user2']
        if usuario1 == str(self.scope['user']):
            self.send(text_data=json.dumps({
                'user1': usuario1,
                'user2': usuario2,
                'userColor':'w',
                'message':'game has been started you are white pieces',
                'startGame':self.Room.pieces
            }))
        elif usuario2 == str(self.scope['user']):
            self.send(text_data=json.dumps({
                'user1': usuario1,
                'user2': usuario2,
                'userColor':'b',
                'message':'game has been started you are black pieces',
                'startGame':self.Room.pieces
            }))
   
    # functios inside function
    def timerHandler(self,who):
        # timer temporário
            if self.Room.tempTimer == 0:
                self.Room.tempTimer = int(self.time()%10000)
                self.Room.save()
                return
            tempTimer = self.Room.tempTimer
            if who == self.Room.user1:
                newTempTimer = int(self.time()%10000)
                self.Room.timer1 = self.Room.timer1 - (newTempTimer-tempTimer)
                self.send(text_data=json.dumps({
                    'message':'o brancho mexeu e o tempo é: {}'.format(self.Room.timer1)
                }))
            elif who == self.Room.user2:
                newTempTimer = int(self.time()%10000)
                self.Room.timer2 = self.Room.timer2 - (newTempTimer-tempTimer)
                self.send(text_data=json.dumps({
                    'message':'o brancho mexeu e o tempo é: {}'.format(self.Room.timer2)
                }))
            self.Room.save()
            self.Room.tempTimer = int(self.time()%10000)




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
        self.timerHandler(data['usuario'])
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
        for line in piecesArray:
            for piece in line:
                if piece == move[0]:
                    #verifica se é um peão
                    if move[0][0] == 'p':
                        #verifica promoção
                        if move[1][2] == '7' and move[1][1] == 'w':
                            move[1] = 'q'+move[1][1]+move[1][2]+move[1][3]
                        elif move[1][2] == '0' and move[1][1] == 'b':
                            move[1] = 'q'+move[1][1]+move[1][2]+move[1][3]
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
                                EnPassant = True
                                self.send(text_data=json.dumps({
                                    'message':'moved',
                                    'enPassant':move
                                }))
                    elif move[0][0] == 'k':
                        movimento = int(move[1][3])
                        if movimento == int(move[0][3])+2 or movimento == int(move[0][3])-2:
                            if movimento == int(move[0][3])+2:
                                move.append(piecesArray[int(move[0][2])][movimento+1])
                                move.append('r'+move[0][1]+move[0][2]+str(movimento-1))
                                piecesArray[int(move[0][2])][int(move[0][3])] = '----'
                                piecesArray[int(move[0][2])][movimento-1] = move[3]
                                piecesArray[int(move[1][2])][int(move[1][3])] = move[1]
                            elif movimento == int(move[0][3])-2:
                                move.append(piecesArray[int(move[0][2])][movimento-2])
                                move.append('r'+move[0][1]+move[0][2]+str(movimento+1))
                                piecesArray[int(move[0][2])][int(move[0][3])] = '----'
                                piecesArray[int(move[0][2])][movimento+1] = move[3]
                                piecesArray[int(move[1][2])][int(move[1][3])] = move[1]
                            self.send(text_data=json.dumps({
                                    'message':'moved',
                                    'castles':move
                                }))

                            EnPassant = True
                    if EnPassant == False:
                        piecesArray[int(piece[2])][int(piece[3])] = '----'
                        piecesArray[int(move[1][2])][int(move[1][3])] = move[1]
                        move_piece = move
                        self.send(text_data=json.dumps({
                            'message':'moved',
                            'movePiece':move_piece
                        }))
                    self.Room.pieces = arrayToStringallPieces(piecesArray)
                    if move[0][1] == 'w':
                        mate = verificarMate(piecesArray,'b')
                    else:
                        mate = verificarMate(piecesArray,'w')
                    if mate:
                        self.send(text_data=json.dumps({
                            'gameEnd':'acabou',
                            'whoLost':mate
                        }))
                        if self.Room.user1 == str(self.scope['user']):
                            print("assasasasasa")
                            historico = GameHistory.objects.create(RoomName=str(self.room_name),
                            user1=self.Room.user1,
                            user2=self.Room.user2,
                            timer1=self.Room.timer1,
                            timer2=self.Room.timer2,
                            history=self.Room.history)
                            print(historico)
                            historico.save()

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        command = text_data_json['command']
        usuario = str(self.scope['user'])
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':command,
                'data':text_data_json,
                'usuario':usuario
            }
        ) 
