from django.core.asgi import get_asgi_application
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_streaming_service.settings')

application = get_asgi_application()
