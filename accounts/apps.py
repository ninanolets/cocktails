from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

    # django docs recomends doing the import this way
    def ready(self):
        import accounts.signals


