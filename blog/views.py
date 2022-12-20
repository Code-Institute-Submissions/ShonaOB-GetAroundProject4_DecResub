from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import TransportReview
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from .forms import PostForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ReviewList(generic.ListView):
    """
    To show all reviews
    """
    model = TransportReview
    queryset = TransportReview.objects.order_by('-created_on')
    template_name = "index.html"
    paginate_by = 6


class ReviewDetail(generic.DetailView):

    """
    To show all reviews
    """
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
            post_form.instance.name = request.user.usename
            post = post_form.save(commit=False)
            post.save()

        return render(
            request,
            "review_detail.html",
            {"review": review,
             "liked": liked,
             },
        )



class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    """
    To show all reviews
    """
    login_url = reverse_lazy('/')
    model = TransportReview
    form_class = PostForm
    template_name = 'post_form.html'

    def form_valid(self, form, *args, **kwargs):
        form.instance.user_name = self.request.user
        success_message = "Created successfully"
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('review_detail', kwargs={'slug': self.object.slug})

    def get_success_message(self, cleaned_data):
        return "Successfully Added!"



class PostLike(generic.DetailView):
    """
    To show all reviews
    """
    def post(LoginRequiredMixin, self, request, slug):
        login_url = 'account_login.html'
        post = get_object_or_404(TransportReview, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('review_detail', args=[slug]))



class UpdatePostView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    """
    To show all reviews
    """
    login_url = 'account_login.html'
    model = TransportReview
    template_name = 'update_post.html'
    fields = ['title', 'review_body', 'featured_image',]

    def get_success_url(self):
        return reverse('review_detail', kwargs={'slug': self.object.slug})

    def get_success_message(self, cleaned_data):
        return "Successfully updated"


class SearchList(generic.ListView):
    """
    To show all reviews
    """
    template_name = 'search.html'
    model = TransportReview

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list



class DeletePostView(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    """
    To show all reviews
    """
    login_url = 'account_login.html'
    model = TransportReview
    template_name = 'delete_review.html'
    
    success_url = reverse_lazy('home')

    def get_success_message(self, cleaned_data):
        return "Successfully Deleted"
