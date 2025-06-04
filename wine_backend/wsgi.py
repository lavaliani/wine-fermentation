import os
from django.core.wsgi import get_wsgi_application

# სწორად ვუთითებთ ბილიკს settings.py-მდე
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wine_backend.settings')

application = get_wsgi_application()
