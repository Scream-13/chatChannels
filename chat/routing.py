from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/<slug:slug>/', consumers.ChatRoomConsumer.as_asgi()),
]