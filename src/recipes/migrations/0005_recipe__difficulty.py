# Generated by Django 4.2.11 on 2024-03-27 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_recipe_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='_difficulty',
            field=models.CharField(default='', max_length=120),
        ),
    ]