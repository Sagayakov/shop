from django.urls import path, include, re_path
from django.views.decorators.cache import cache_page
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'shop', ShopViewSet)
print(router.urls)


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('phone/<slug:phone_slug>', PhoneView.as_view(), name='phone_link'),
    path('brand/<slug:mark_slug>', MarkView.as_view(), name='mark_link'),
    path('register', RegisterUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
]
