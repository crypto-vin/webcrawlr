from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY='dev'
DEBUG = False
ALLOWED_HOSTS = ['*']  # for testing; change to your domain later
STATIC_ROOT = BASE_DIR / "staticfiles"  # Render needs this

INSTALLED_APPS=['django.contrib.contenttypes','django.contrib.staticfiles','core']
MIDDLEWARE=[]
ROOT_URLCONF='webagency.urls'
TEMPLATES=[{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':['templates'],'APP_DIRS':True,'OPTIONS':{}}]
WSGI_APPLICATION='webagency.wsgi.application'
STATIC_URL='/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static"
]