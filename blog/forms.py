from django_summernote.widgets import SummernoteWidget
from django_summernote.fields import SummernoteTextFormField
from .models import TransportReview
from django import forms


class PostForm(forms.ModelForm):
    """
    Sets the model and fields for Review Form. 
    Provides front-end user with Summernote
    """
    class Meta: 
        model = TransportReview
        fields = ('country', 'city', 'sight', 'transport_option', 'title', 'featured_image', 'rating', 'review_body',)
        widgets = {
            'review_body': SummernoteWidget(),
        }