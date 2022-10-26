import json
from tkinter import N
from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async

from my_social_app.models import User


class MySyncConsumer(SyncConsumer):
    # channel_layer = get_channel_layer()
    def websocket_connect(self, event):
        print("websocket is connected..", event)
        print("channel layer is ..", self.channel_layer)
        print("channel name is ..", self.channel_name)
        async_to_sync(self.channel_layer.group_add)(
            'programmers', self.channel_name)
        self.send({
            'type': 'websocket.accept'
        })

    def websocket_receive(self, event):
        print("websocket is Received..", event['text'])
        print("type of websocket is Received ..", type(event['text']))
        async_to_sync(self.channel_layer.group_send)('programmers', {
            'type': 'chat.message',
            'message': event['text']
        })

    def chat_message(self, event):
        print("event is...", event)
        print("Actual event is...", event['message'])
        print("type of Actual event is...", type(event['message']))
        self.send({
            'type': 'websocket.send',
            'text': event['message']
        })

    def websocket_disconnect(self, event):
        print("websocket is disconnected..", event)
        async_to_sync(self.channel_layer.group_discard)(
            'programmers', self.channel_name)
        raise StopConsumer()


class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("websocket is connected123..", event)
        user= self.scope['user']
        print('user')
        chat_room= f'user_chatroom_{user.id}'
        self.chat_room= chat_room
        await self.channel_layer.group_add(
            chat_room,
            self.channel_name
        )
        await  self.send({
            'type': 'websocket.accept'
        })

    async def websocket_receive(self, event):
        print("websocket is Received..", event)
        received_data=json.loads(event['text'])
        msg= received_data.get('message')
        sent_by_id=received_data.get('sent_by')
        send_to_id=received_data.get('send_to')
        # sent_by= json.loads(sent_by)
        # send_to= json.loads(send_to)
        # sent_by_id= sent_by.id
        # send_to_id= send_to.id
        print(send_to_id, sent_by_id)

        
        if not msg:
            print('Error:: empty message')
            return False
        sent_by_user= await self.get_user_objects(sent_by_id)
        send_to_user= await self.get_user_objects(send_to_id)
        if not sent_by_user:
            print('Error:: sent by  user is incorrect')
        if not send_to_user:
            print('Error:: send to user is incorrect')
        

        other_user_in_chat_room= f'user_chatroom_{send_to_id}'
        self_user= self.scope['user']  #not workink 
        # print(self_user, "self user is ")

        response={
            "message": msg,
            "sent_by":sent_by_user.id
        }
        await self.channel_layer.group_send(
            other_user_in_chat_room,
            {
                'type': 'chat_message',
                'text':json.dumps(response)
            }
        )
        await self.channel_layer.group_send(
            self.chat_room,
            {
                'type': 'chat_message',
                'text':json.dumps(response)
            }
        )
   
    async def chat_message(self, event):
        print("chat message", event['text'])
        await self.send({
            'type':'websocket.send',
            'text':event['text']
        })
    async def websocket_disconnect(self, event):
        print("websocket is disconnected..", event)
        raise StopConsumer()



    @database_sync_to_async 
    def get_user_objects(self, user_id):
        queryset= User.objects.filter(id= user_id)
        print(queryset,"user data for message")
        if queryset.exists():
            object= queryset.first()
            print(object.id, 'object')

        else:
            object= None
        return object        
             
