from django.shortcuts import render, get_object_or_404
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


class ReviewDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = TransportReview.objects.order_by('-created_on')
        review = get_object_or_404(queryset, slug=slug)
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "review_detail.html",
            {"review": review,
            "liked": liked,
            },
        )
