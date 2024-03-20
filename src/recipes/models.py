from django.db import models
from django.shortcuts import reverse

class Recipe(models.Model):
    name =  models.CharField(max_length=100)
    cooking_time = models.IntegerField(help_text='in min', default=0)
    ingredients = models.CharField(max_length=250)
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')
    author = models.CharField(max_length=120, default='anonym')
    instructions = models.TextField(default="No instructions ...")

    def __str__(self):
        return f"{self.name} - {self.difficulty} - {self.cooking_time}"
    
    def get_absolute_url(self):
        return reverse ('recipes:detail', kwargs={'pk': self.pk})
    
    @property
    def difficulty(self):
        ingredients_len = len(self.ingredients.split(", "))
        if self.cooking_time < 10 and ingredients_len < 4:
            return "Easy"
        elif self.cooking_time < 10 and ingredients_len >= 4:
            return "Medium"
        elif self.cooking_time >= 10 and ingredients_len < 4:
            return "Intermediate"
        elif self.cooking_time >= 10 and ingredients_len >= 4:
            return "Hard"