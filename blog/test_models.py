from django.test import TestCase
from .models import TransportReview, Country, CityName, Sight, User


class TestModels(TestCase):
    def test_done_defaults_to_false(self):
        country = Country(country_name='TestCountry')
        country.save()
        city = CityName(city_name='testcity', location=country)
        city.save()
        sight = Sight(sight_name='testsight', sight_location=city)
        sight.save()
        user = User.objects.create(
            username='administratortest', password='yhcranason32')
        user.save()
        review = TransportReview.objects.create(
            country=country,
            city=city,
            sight=sight,
            transport_option='bus',
            title='test title',
            slug='test_title',
            rating='1',
            created_on='Aug. 27, 2022, 8:52 a.m.',
            user_name=user,
            review_body='test body text',
        )
        self.assertFalse(review.done)
