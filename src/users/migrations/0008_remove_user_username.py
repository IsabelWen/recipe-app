# Generated by Django 4.2.11 on 2024-03-21 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_user_user_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
