from base import *

SECRET_KEY = 'sp(j(ts6ri()muwz-$^i+k+jgjfv$jbgs@9oq@lzy6x5@lynqd'

INSTALLED_APPS += [
    'django_extensions',
]

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
