# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Room
class RoomConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.Room,created = Room.objects.get_or_create(code=self.room_group_name)
        if(created):
            print("novo")
        print(self.Room.pieces)
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
        self.start_game(self)

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
        self.send(text_data=json.dumps({
            'message':'game has been started',
            'piece':self.Room.pieces
        }))

    def move_piece(self,data):
        pieces = data['data']['pieces_value']
        self.Room.pieces = pieces
        self.Room.save()
    commands = {
        'chat_message':chat_message,
        'start_game':start_game,
        'move_piece':move_piece,
    }
    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        command = text_data_json['command']
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': command,
                'data':text_data_json
            }
        )