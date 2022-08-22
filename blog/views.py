from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    View,
    DetailView,
    CreateView,
    UpdateView)
from .models import TransportReview
from django.http import HttpResponseRedirect
from .forms import PostForm
from django.urls import reverse


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

    def post(self, request, slug, *args, **kwargs):
        queryset = TransportReview.objects.order_by('-created_on')
        review = get_object_or_404(queryset, slug=slug)
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True

        post_form = PostCreateView(data=request.POST)

        if post_form.is_valid():
            post_form.instance.email = request.user.email
            post_form,instance.name = request.user.usename
            post = post_form.save(commit=False)
            post.save()


        return render(
            request,
            "review_detail.html",
            {"review": review,
            "liked": liked,
            },
        )

class PostCreateView(CreateView):
    model = TransportReview
    form_class = PostForm
    template_name = 'post_form.html'

    def form_valid(self, form, *args, **kwargs):
        form.instance.user_name = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('review_detail', kwargs={'slug': self.object.slug})


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(TransportReview, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('review_detail', args=[slug]))


class UpdatePostView(UpdateView):
    model = TransportReview
    template_name = 'update_post.html'
    fields = ['title', 'review_body', 'featured_image']

    def get_success_url(self):
        return reverse('review_detail', kwargs={'slug': self.object.slug})