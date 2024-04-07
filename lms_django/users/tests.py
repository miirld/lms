from django.test import TestCase
from .models import CustomUser

class Test_CustomUser_Model(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = CustomUser.objects.create(username='test', password='1234test')

    def test_user(self):
            user = CustomUser.objects.get(id=1)
            username = f'{user.username}'
            password = f'{user.password}'
            self.assertEqual(username, 'test')
            self.assertEqual(password, '1234test')
            self.assertEqual(str(user), 'test')
