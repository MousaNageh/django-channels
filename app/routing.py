

from django.urls import path
from .consumer import EchoConsumer

urls = [
  path("ws/chat/",EchoConsumer.as_asgi())
]