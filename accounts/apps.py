from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        # Registers the pre_save signal that auto-creates a Profile
        # for every new CustomUser.
        import accounts.signals  # noqa: F401