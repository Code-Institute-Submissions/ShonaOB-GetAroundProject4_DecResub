from django.test import TestCase
from .models import TransportReview, Country, CityName, Sight, User
from django.urls import reverse


class TestViews(TestCase):

    def test_get_review_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_add_review_page(self):
        url = reverse('post_form')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_form.html')


