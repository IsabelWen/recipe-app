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

    def __str__(self):
        return f"{self.name} - {self.difficulty} - {self.cooking_time}"