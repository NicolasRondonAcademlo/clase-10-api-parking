# Generated by Django 3.2 on 2022-05-18 00:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0004_alter_rack_uuid_rackitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rack',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('ce6fd80c-ad60-4fc0-b409-5f044d58841d')),
        ),
    ]
