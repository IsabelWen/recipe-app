# Generated by Django 4.2.11 on 2024-03-26 11:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_recipe_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
