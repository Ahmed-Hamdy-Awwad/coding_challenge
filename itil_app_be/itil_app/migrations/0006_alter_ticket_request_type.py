# Generated by Django 3.2.4 on 2022-08-12 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itil_app', '0005_auto_20210622_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='request_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='itil_app.requesttype'),
        ),
    ]
