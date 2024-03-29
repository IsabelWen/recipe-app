from django.test import TestCase, Client
from .models import Recipe
from .forms import RecipesSearchForm, CreateRecipeForm
from django.utils import timezone
from datetime import date
from django.urls import reverse
from users.models import User

# Test model
class RecipeModelTest(TestCase):
    def setUpTestData():
        Recipe.objects.create(
            name='Banana Pancakes', 
            cooking_time=8, 
            ingredients='Banana, Eggs, Baking Powder',
            date_created=timezone.now())
        
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

    # test to see if date_created is initialized as expected
    def test_date_created(self):
        recipe = Recipe.objects.get(id=1)
        self.assertIsInstance(recipe.date_created, date)
        self.assertEqual(recipe.date_created.year, timezone.now().date().year)
        self.assertEqual(recipe.date_created.month, timezone.now().date().month)
        self.assertEqual(recipe.date_created.day, timezone.now().date().day)

    # test to see if calculate_difficulty works 
    def test_calculate_difficulty(self):
        # When time >= 10 min and ingredients < 4 difficulty should be 'Intermediate'
        recipe = Recipe(cooking_time=15, ingredients="Ingredient 1, Ingredient 2")
        self.assertEqual(recipe.difficulty, "Intermediate")

# Test auth
class RecipeAuthTest(TestCase):
    def setUpTestData():
        Client()
        user = User.objects.create_user(username='testuser', password='testpassword')
        Recipe.objects.create(
            name='Banana Pancakes',
            ingredients='Banana, Eggs, Baking Powder',
            author=user)
    # without auth
    def test_details_redirect_without_auth(self):
        recipe = Recipe.objects.get(id=1)
        response = self.client.get(reverse('recipes:detail', args=[recipe.id]))
        self.assertRedirects(response, f'/login/?next={reverse("recipes:detail", args=[recipe.id])}')
    
    def test_author_redirect_without_auth(self):
        recipe = Recipe.objects.get(id=1)
        response = self.client.get(reverse('recipes:author', args=[recipe.id]))
        self.assertRedirects(response, f'/login/?next={reverse("recipes:author", args=[recipe.id])}')

    # with auth
    def test_list_redirect_with_auth(self):
        login = self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('recipes:recipes'))
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipes_list.html')

    def test_details_redirect_with_auth(self):
        login = self.client.login(username='testuser', password='testpassword')
        recipe = Recipe.objects.get(id=1)
        response = self.client.get(reverse('recipes:detail', args=[recipe.id]))
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipes_details.html')

    def test_author_redirect_with_auth(self):
        login = self.client.login(username='testuser', password='testpassword')
        recipe = Recipe.objects.get(id=1)
        response = self.client.get(reverse('recipes:author', args=[recipe.id]))
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipes_author.html')


# Test forms
class RecipeFormsTest(TestCase):
    def setUpTestData():
        user = User.objects.create_user(username='testuser', password='testpassword')
        Recipe.objects.create(
            name='Test Recipe',
            cooking_time=30,
            ingredients='Ingredient 1, Ingredient 2',
            instructions='Step 1, Step 2',
            pic='test_pic.jpg',
            author=user
        )
    
    def test_recipes_search_form(self):
        form_data = {'recipe_name': 'Pancakes', 'chart_type': 'bar_chart'}
        form = RecipesSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_create_recipe_form(self):
        form_data = Recipe.objects.get(id=1).__dict__
        form = CreateRecipeForm(data=form_data)
        self.assertTrue(form.is_valid())
        

