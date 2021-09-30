
# chat/consumers.py
import json
from main.game.game import selectPiece
from main.game.ConvertStringArray import arrayToStringallPieces, arrayTostring, stringToArray
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Room
from channels.layers import get_channel_layer

class RoomConsumer(WebsocketConsumer):
    def connect(self):
        self.userName = self.scope['user']
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.Room,created = Room.objects.get_or_create(roomCode=self.room_group_name)
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()


    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from room group
    def chat_message(self, event):
        print("message")
        message = event['data']['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))

    def start_game(self,data):
        if data['filter'] == self.channel_name:
            self.send(text_data=json.dumps({
                'user':str(self.userName),
                'message':self.channel_name,
                'startGame':self.Room.pieces
            }))

    def select_piece(self,data):
        #recolhe a peça que foi selecionada
        piece = data['data']['piece']
        #recolhe todas as peças no backend
        allPieces = stringToArray(self.Room.pieces)
        #checa se a peça existe
        for line in allPieces:
            for pieceInBack in line:
                if pieceInBack == piece:
                    #se a peça existir vou retornar o movimentos possíveis caso haja se não apenas retorno a peça
                    moves = selectPiece(allPieces,piece)
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
        #executa os movimentos para a peça selecionada
       

    def move_piece(self,data):
        move = data['data']['move']
        move = move.split(' ')
        pieces = self.Room.pieces
        piecesArray = stringToArray(pieces)
        for line in piecesArray:
            for piece in line:
                if piece == move[0]:
                    piecesArray[int(piece[2])][int(piece[3])] = '----'
                    piecesArray[int(move[1][2])][int(move[1][3])] = move[1]
                    self.Room.pieces = arrayToStringallPieces(piecesArray)
                    move_piece = move
                    self.send(text_data=json.dumps({
                        'message':'moved',
                        'movePiece':move_piece
                    }))
                    return

    commands = {
        'chat_message':chat_message
    }




    # Receive message from WebSocket
    def receive(self, text_data):
        print(self.channel_name)
        text_data_json = json.loads(text_data)
        command = text_data_json['command']
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':command,
                'data':text_data_json,
                'filter':self.channel_name
            }
        )