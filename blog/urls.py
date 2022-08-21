from . import views
from .views import PostCreateView, ListView, DetailView
from django.urls import path


urlpatterns = [
    path('', views.ReviewList.as_view(), name='home'),
    path('views/', views.PostCreateView.as_view(), name='post_form'),
    path('<slug:slug>/', views.ReviewDetail.as_view(), name='review_detail'),

]