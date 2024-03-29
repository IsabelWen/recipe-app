# Generated by Django 4.2.11 on 2024-03-23 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='pic',
            field=models.ImageField(default='no_picture.jpg', help_text='Choose an image with minimum 250px width.', upload_to='recipes'),
        ),
    ]