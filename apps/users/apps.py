from django.apps import AppConfig
from django.db.models.signals import post_migrate

def config_app(sender, **kwargs):
    from django.conf import settings
    from django.contrib.auth import get_user_model
    

    from apps.project.models import ROL_NAME_ADMIN

    
    User = get_user_model()
    if User.objects.all().count() == 0:
        user = User.objects.create_superuser(
            username=settings.DJANGO_SUPERUSER_USERNAME,
            email=settings.DJANGO_SUPERUSER_EMAIL,
            first_name=settings.DJANGO_SUPERUSER_FIRST_NAME,
            last_name=settings.DJANGO_SUPERUSER_LAST_NAME,
            password=settings.DJANGO_SUPERUSER_PASSWORD,
        )
        

class UsersConfig(AppConfig):
    name = "apps.users"

    def ready(self):
        post_migrate.connect(config_app, sender=self)
