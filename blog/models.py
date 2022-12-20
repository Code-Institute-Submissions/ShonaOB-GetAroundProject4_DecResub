from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


class Country(models.Model):
    country_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['country_name']

    def __str__(self):
        return self.country_name


class CityName(models.Model):
    city_name = models.CharField(max_length=100, unique=True)
    location = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        ordering = ['city_name']

    def __str__(self):
        return self.city_name


class Sight(models.Model):
    sight_name = models.CharField(max_length=100, unique=True)
    sight_location = models.ForeignKey(CityName, on_delete=models.CASCADE)

    class Meta:
        ordering = ['sight_name']

    def __str__(self):
        return self.sight_name


class TransportReview(models.Model):
    """ Create a database for the transport reviews """

    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    BUS = 'BUS'
    TRAIN = 'TR'
    UNDERGROUND = 'UGR'
    TRAM = 'TRAM'
    WALK = 'WALK'
    TRANSPORT_CHOICES = [
        (BUS, 'Bus'),
        (TRAIN, 'Train'),
        (UNDERGROUND, 'Underground'),
        (TRAM, 'Tram'),
        (WALK, 'Walk'),
    ]

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(CityName, on_delete=models.CASCADE)
    sight = models.ForeignKey(Sight, on_delete=models.CASCADE)
    transport_option = models.CharField(
        max_length=200, choices=TRANSPORT_CHOICES)
    title = models.CharField(max_length=200, unique=True, default='Title')
    slug = models.SlugField(max_length=200, unique=True)
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    review_body = models.TextField(max_length=5000)
    featured_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateField(auto_now=True)
    likes = models.ManyToManyField(User, related_name="likes", blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
