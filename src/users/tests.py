from django.test import TestCase
from .models import User

# Create your tests here.
class UserModelTest(TestCase):
    def setUpTestData():
        User.objects.create(name='Max Mustermann', username='testuser')
        
    # test to see if the user's name is initialized as expected
    def test_recipe_name(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    # test to see if the length of the name field is a maximum of 120 characters 
    def test_user_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('name').max_length
        self.assertEqual(max_length, 120, 'name has over 120 characters')

    # test to see if the length of the username field is a maximum of 120 characters 
    def test_user_username_max_length(self):
        username = User.objects.get(id=1)
        max_length = username._meta.get_field('username').max_length
        self.assertEqual(max_length, 120, 'username has over 120 characters')