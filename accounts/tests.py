from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUsernameValidatorTests(TestCase):
    """Test custom username validation"""
    
    def test_username_with_plus_allowed(self):
        user = User.objects.create_user(username='user+test', password='pass')
        self.assertEqual(user.username, 'user+test')

    def test_username_with_hyphen_allowed(self):
        user = User.objects.create_user(username='user-test', password='pass')
        self.assertEqual(user.username, 'user-test')

    def test_username_with_underscore_allowed(self):
        user = User.objects.create_user(username='user_test', password='pass')
        self.assertEqual(user.username, 'user_test')

    def test_username_with_numbers_allowed(self):
        user = User.objects.create_user(username='user123', password='pass')
        self.assertEqual(user.username, 'user123')