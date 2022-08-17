# Generated by Django 3.2.15 on 2022-08-17 17:30

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CityName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ['city_name'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['country_name'],
            },
        ),
        migrations.CreateModel(
            name='Sight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sight_name', models.CharField(max_length=100, unique=True)),
                ('sight_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.cityname')),
            ],
            options={
                'ordering': ['sight_name'],
            },
        ),
        migrations.CreateModel(
            name='TransportReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transport_option', models.CharField(choices=[('BUS', 'Bus'), ('TR', 'Train'), ('UGR', 'Underground'), ('TRAM', 'Tram'), ('WALK', 'Walk')], max_length=200)),
                ('title', models.CharField(default='Title', max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('review_body', models.TextField(max_length=5000)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('updated_on', models.DateField(auto_now=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.cityname')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.country')),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('sight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.sight')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.AddField(
            model_name='cityname',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.country'),
        ),
    ]