from django.test import TestCase
from service.account.models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('unique@email.com', 'unique')

    def test_create_user_with_valid_email_can_be_created(self):
        try:
            user = User.objects.create_user(email='abc@abc.com', password='test_password_123')
            superuser = User.objects.create_superuser(
                email='xyz@xyz.com', password='test_password_123'
            )
        except Exception:
            self.fail('user creation fails unexpectedly')

        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)

    def test_fail_used_email_user_creation(self):
        with self.assertRaises(Exception):
            User.objects.create_user('unique@email.com', 'abcde')

        with self.assertRaises(Exception):
            User.objects.create_superuser('unique@email.com', 'edcba')

    def test_faild_invalid_email_user(self):
        with self.assertRaises(Exception):
            User.objects.create_superuser('abc', 'edcba')

        with self.assertRaises(Exception):
            User.objects.create_superuser('a123a@', 'abc')

        with self.assertRaises(Exception):
            User.objects.create_superuser('@mail.com', 'aaa')

        with self.assertRaises(Exception):
            User.objects.create_superuser('@', 'duf')
