from django.apps import AppConfig


class CitiesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cities'
    verbose_name = 'Населенные пункты'


class CustomAuthConfig(AppConfig):
    name = 'django.contrib.auth'
    verbose_name = 'Имя изменил в app.py'
