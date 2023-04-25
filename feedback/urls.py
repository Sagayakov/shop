from django.urls import path, include

from .views import *

urlpatterns = [
    path('', FeedbackView.as_view(), name='feedback'),
    path('api/v1/usr-auth/', include('rest_framework.urls')),
    path('api/v1/feedback/', FeedbackAPIList.as_view()),
    path('api/v1/feedback/<int:pk>/', FeedbackAPIUpdate.as_view()),
    path('api/v1/feedbackdelete/<int:pk>/', FeedbackAPIDestroy.as_view()),
    path('done', DoneFeedbackView.as_view(), name='done')
]
