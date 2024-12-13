# Generated by Django 5.1.3 on 2024-12-12 13:09

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userregister'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregister',
            name='register_token',
            field=models.UUIDField(default=uuid.uuid4, verbose_name='Ссылка-токен'),
        ),
    ]