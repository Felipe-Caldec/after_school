from django.apps import AppConfig


class AfterAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'after_app'
