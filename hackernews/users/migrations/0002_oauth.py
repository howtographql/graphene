from django.db import migrations
from django.core.management import call_command
from oauth2_provider.models import get_application_model

Application = get_application_model()


def create_application(apps, schema_editor):
    application = Application(
        name="HackerNews Client",
        redirect_uris="http://localhost http://example.com http://example.org",
        user=None,
        client_type=Application.CLIENT_CONFIDENTIAL,
        authorization_grant_type=Application.GRANT_AUTHORIZATION_CODE, )
    application.save()


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_application),
    ]
