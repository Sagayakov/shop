# from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics

from .models import FeedbackModel
from .forms import FeedbackForm
from .permissions import *
from .serializers import FeedbackSerializer


class FeedbackView(CreateView):
    model = FeedbackModel
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = reverse_lazy('done')  # хардкод или лэйзи, просто реверс не успевает формировать ссылку


class DoneFeedbackView(TemplateView):
    template_name = 'feedback/done.html'


class FeedbackAPIList(generics.ListCreateAPIView):
    queryset = FeedbackModel.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class FeedbackAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = FeedbackModel.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class FeedbackAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = FeedbackModel.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (IsAdminOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
