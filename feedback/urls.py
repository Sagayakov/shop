from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', FeedbackView.as_view(), name='feedback'),
    path('done', DoneFeedbackView.as_view(), name='done')
]
