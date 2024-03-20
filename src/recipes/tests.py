from django.test import TestCase
from .models import Recipe

# Create your tests here.
class RecipeModelTest(TestCase):
    def setUpTestData():
        Recipe.objects.create(
            name='Banana Pancakes', 
            cooking_time=8, 
            ingredients='Banana, Eggs, Baking Powder')
        
    # test to see if the recipe's name is initialized as expected
    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')
    
    # test to see if the default image is used if no other pic uploaded
    def test_recipe_pic(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.pic, 'no_picture.jpg')

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

    # test to see if function for getting the recipe details url works
    def test_get_absolute_url(self):
       recipe = Recipe.objects.get(id=1)
       #get_absolute_url() should take you to the detail page of recipe #1
       #and load the URL /recipes/1
       self.assertEqual(recipe.get_absolute_url(), '/recipes/1')

    # test to see if calculate_difficulty works
    def test_calculate_difficulty(self):
        # When time >= 10 min and ingredients < 4 difficulty should be 'Intermediate'
        recipe = Recipe(cooking_time=15, ingredients="Ingredient 1, Ingredient 2")
        self.assertEqual(recipe.difficulty, "Intermediate")
    