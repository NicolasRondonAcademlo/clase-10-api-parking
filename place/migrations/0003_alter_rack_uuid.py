# Generated by Django 4.0.4 on 2022-05-16 16:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0002_rack_status_alter_rack_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rack',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('5b9bc511-70a8-4f5e-a046-5db20f193fef')),
        ),
    ]