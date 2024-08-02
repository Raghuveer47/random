from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/randomcall/(?P<room_id>\w+)/$', consumers.RandomCallConsumer.as_asgi()),
]
