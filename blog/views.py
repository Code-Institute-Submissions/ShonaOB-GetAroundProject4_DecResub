from django.shortcuts import render
from django.views import generic
from .models import TransportReview

class ReviewList(generic.ListView):
    model = TransportReview
    queryset = TransportReview.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6
    
