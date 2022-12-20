from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import TransportReview
from .models import Country
from .models import CityName
from .models import Sight


@admin.register(TransportReview)
class TransportReviewAdmin(SummernoteModelAdmin):
    summernote_fields = ('review_body')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('country', 'created_on')
    list_display = ('title', 'country', 'created_on')
    search_fields = ('country', 'city', 'sight', 'title', 'rating')


admin.site.register(Country)

admin.site.register(CityName)

admin.site.register(Sight)
