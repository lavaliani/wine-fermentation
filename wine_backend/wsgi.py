import os
from django.core.wsgi import get_wsgi_application

# სწორი ბილიკი, რომელიც მიუთითებს 'settings.py' ფაილზე
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wine-fermentation.settings')

application = get_wsgi_application()
