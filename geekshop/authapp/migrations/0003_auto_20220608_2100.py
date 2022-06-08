# Generated by Django 3.2.11 on 2022-06-08 18:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_alter_shopuser_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='activation_key',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 10, 18, 0, 41, 130202, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='активный'),
        ),
    ]
