from django.test import TestCase
from .models import CustomUser
from django.contrib.auth.models import User

# Create your tests here.
class UserModelTest(TestCase):
    def setUpTestData():
        user = User.objects.create_user(username='maxmustermann', password='testpassword')
        CustomUser.objects.create(user=user, name='Max Mustermann', bio='Hi, I am Max Mustermann.')
        
    # test to see if the user's name is initialized as expected
    def test_user_name(self):
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    # test to see if the default image is used if no other pic uploaded
    def test_users_pic(self):
        user = CustomUser.objects.get(id=1)
        self.assertEqual(user.pic, 'no_picture.jpg')

    # test to see if the length of the name field is a maximum of 120 characters 
    def test_user_name_max_length(self):
        user = CustomUser.objects.get(id=1)
        max_length = user._meta.get_field('name').max_length
        self.assertEqual(max_length, 120, 'name has over 120 characters')

    # test to see if the length of the username field is a maximum of 120 characters 
    def test_user_username_max_length(self):
        user = CustomUser.objects.get(id=1)
        max_length = user.user._meta.get_field('username').max_length
        self.assertEqual(max_length, 150, 'username has over 120 characters')

    # test to see if the user's bio is initialized as expected
    def test_user_bio(self):
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field('bio').verbose_name
        self.assertEqual(field_label, 'bio')