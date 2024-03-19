from django.db import models

# Create your models here.
difficulty_choices= (
    ('Easy', 'easy'), 
    ('Medium', 'medium'), 
    ('Intermediate', 'intermediate'), 
    ('Hard', 'hard'),
)

class Recipe(models.Model):
    name =  models.CharField(max_length=100)
    cooking_time = models.IntegerField(help_text='in min', default=0)
    ingredients = models.CharField(max_length=250)
    difficulty = models.CharField(max_length=12, choices=difficulty_choices, default=difficulty_choices[0][0])
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')
    author = models.CharField(max_length=120, default='anonym')
    instructions = models.TextField(default="No instructions ...")

    def __str__(self):
        return f"{self.name} - {self.difficulty} - {self.cooking_time}"