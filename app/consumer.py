from channels.consumer import SyncConsumer
from asgiref.sync import async_to_sync
class EchoConsumer(SyncConsumer):
  def websocket_connect(self, event):
        self.roomName = "chatRoom"
        self.send({
            "type": "websocket.accept",
        })
        async_to_sync(self.channel_layer.group_add)(self.roomName,self.channel_name)
  def websocket_receive(self, event):
        print(event["text"])
        async_to_sync(self.channel_layer.group_send)(
          self.roomName,
          {
            "type": "websocket.message",
            "text": event.get("text"),
          }
          
          )
  
  def websocket_message(self,event): 
      self.send({
            "type": "websocket.send",
            "text": event.get("text"),
        })
  
  def websocket_disconnect(self, event):
        print("disconnect  ")
        async_to_sync(self.channel_layer.group_discard)(self.roomName,self.channel_name)
        print(event)