from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('phone/<slug:phone_slug>', PhoneView.as_view(), name='phone_link'),
    path('brand/<slug:mark_slug>', MarkView.as_view(), name='mark_link')
]
