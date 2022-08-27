from django.test import TestCase
from .forms import PostForm


class TestPostForm(TestCase):

    def form_country_is_required(self):
        form = PostForm({"country": ""})
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(form.errors['country'][0], 'This field is required.')

    def form_city_is_required(self):
        form = PostForm({"city": ""})
        self.assertFalse(form.is_valid())
        self.assertIn('city', form.errors.keys())
        self.assertEqual(form.errors['city'][0], 'This field is required.')

    def form_sight_is_required(self):
        form = PostForm({"sight": ""})
        self.assertFalse(form.is_valid())
        self.assertIn('sight', form.errors.keys())
        self.assertEqual(form.errors['sight'][0], 'This field is required.')
