from django.test import TestCase
from .models import MyUser

# Create your tests here.

class MyUserModelTests(TestCase):
    def test_get_fio_basic(self):
        """
        Test a basic scenario with all fields present.
        """
        user = MyUser(last_name='Testovov', first_name='Test', patronymic='Testovich')
        self.assertEqual(user.get_fio(), 'Testovov Test Testovich')

    def test_get_fio_last_name_missing(self):
        """
        Test when last_name is missing.
        """
        user = MyUser(first_name='Test', patronymic='Testovich')
        self.assertEqual(user.get_fio(), 'Test Testovich')

    def test_get_fio_first_name_missing(self):
        """
        Test when first_name is missing.
        """
        user = MyUser(last_name='Testovov', patronymic='Testovich')
        self.assertEqual(user.get_fio(), 'Testovov Testovich')

    def test_get_fio_patronymic_missing(self):
        """
        Test when patronymic is missing.
        """
        user = MyUser(last_name='Testovov', first_name='Test')
        self.assertEqual(user.get_fio(), 'Testovov Test')

    def test_get_fio_all_fields_missing(self):
        """
        Test when all fields are missing.
        """
        user = MyUser()
        self.assertEqual(user.get_fio(), '')

    def test_get_fio_with_spaces(self):
        """
        Test with leading/trailing whitespaces in fields.
        """
        user = MyUser(last_name='  Last  ', first_name='  First  ', patronymic='  Patronymic  ')
        self.assertEqual(user.get_fio(), 'Last First Patronymic')

    def test_get_fio_unicode_characters(self):
        """
        Test with Unicode characters in fields.
        """
        user = MyUser(last_name='李', first_name='王', patronymic='张')
        self.assertEqual(user.get_fio(), '李 王 张')
