from novahack.settings.docker import * # noqa F401 F403
from dotenv import load_dotenv
import os

load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("POSTGRES_NOVA_DB"),
        'USER': os.getenv("POSTGRES_NOVA_USER"),
        'PASSWORD': os.getenv("POSTGRES_NOVA_PASSWORD"),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
