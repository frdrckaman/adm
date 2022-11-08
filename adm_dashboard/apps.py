from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'adm_dashboard'
    verbose_name = "ADM Dashboard"
