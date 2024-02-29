from decouple import config


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD', cast=int),
        'HOST': config('DATABASE_HOST'),
        'PORT': config('DATABASE_PORT', cast=int),
    }
}
