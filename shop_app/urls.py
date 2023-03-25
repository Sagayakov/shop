from django.urls import path
# from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('phone/<slug:phone_slug>', PhoneView.as_view(), name='phone_link'),
    path('brand/<slug:mark_slug>', MarkView.as_view(), name='mark_link'),
    path('register', RegisterUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
]
