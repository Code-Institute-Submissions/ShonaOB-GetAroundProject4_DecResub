from django.shortcuts import render
from django.views.generic import (
    ListView,
    View,
    DetailView,
    CreateView)
from .models import TransportReview


class ReviewList(ListView):
    model = TransportReview
    queryset = TransportReview.objects.order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6

