# Generated by Django 3.2.4 on 2022-08-12 13:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('itil_app', '0006_alter_ticket_request_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='reporter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ticket_reporter', to=settings.AUTH_USER_MODEL),
        ),
    ]