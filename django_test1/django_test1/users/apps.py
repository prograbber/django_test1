from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "django_test1.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import django_test1.users.signals  # noqa F401
        except ImportError:
            pass
