from django.test import TestCase
from .models import Recipe

# Create your tests here.
class RecipeModelTest(TestCase):
    def setUpTestData():
        Recipe.objects.create(name='Banana Pancakes', cooking_time=10, 
                              ingredients='Banana, Eggs, Baking Powder', difficulty='Medium')
        
    # test to see if the recipe's name is initialized as expected
    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    # test to see if the length of the name field is a maximum of 100 characters 
    def test_recipe_name_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('name').max_length
        self.assertEqual(max_length, 100, 'name has over 100 characters')

    # test to see if the cooking_time field is an integer
    def test_cooking_time_is_integer(self):
        recipe = Recipe.objects.get(id=1)
        cooking_time = recipe.cooking_time
        self.assertIs(type(cooking_time), int, 'cooking_time is not a number')

    # test to see if the length of the ingredients field is a maximum of 250 characters 
    def test_ingredients_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('ingredients').max_length
        self.assertEqual(max_length, 250, 'ingredients has over 250 characters')

    # test to see if the length of the difficulty field is a maximum of 12 characters 
    def test_difficulty_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('difficulty').max_length
        self.assertEqual(max_length, 12, 'difficulty has over 12 characters')