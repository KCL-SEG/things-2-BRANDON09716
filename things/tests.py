from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .forms import MyForm
class MyFormTest(TestCase):
    def test_form_validity(self):
        form_data = {'name': 'Brandon Zhang', 'email': 'Zhang@example.com', 'age': 20,'comment':'Test'}
        form = MyForm(data=form_data)
        self.assertTrue(form.is_valid())


