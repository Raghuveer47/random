import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import videoconference_app.routing  # Replace with your app name

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'videoconferencing.settings')  # Replace with your project name

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            videoconference_app.routing.websocket_urlpatterns  # Replace with your app name
        )
    ),
})
