from django.apps import AppConfig

class StartConfig(AppConfig):
    name = 'start'

    def ready(self):
        import start.signals