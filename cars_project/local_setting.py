# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-nh$q-2jm=bei+k4zr5k)7zb3(!zm0h@_h=&9*y8!s*bo0+m!&^'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD':'Password10'

    }
}
