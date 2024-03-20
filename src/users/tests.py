from django.test import TestCase
from .models import User

# Create your tests here.
class UserModelTest(TestCase):
    def setUpTestData():
        User.objects.create(name='Max Mustermann', username='testuser', bio='Hi, I am Max Mustermann.')
        
    # test to see if the user's name is initialized as expected
    def test_user_name(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    # test to see if the default image is used if no other pic uploaded
    def test_users_pic(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.pic, 'no_picture.jpg')

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

    # test to see if the user's bio is initialized as expected
    def test_user_bio(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('bio').verbose_name
        self.assertEqual(field_label, 'bio')