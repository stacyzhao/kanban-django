# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1d-cdr&jnxzyrn@+m9_r4+*eg4#mjbw76!p223al6^pdp@jcx('

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tasks',
        'USER': 'stacy',
        'PASSWORD': 'greentea',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
