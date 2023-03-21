# from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

from .models import FeedbackModel
from .forms import FeedbackForm


# Create your views here.

class FeedbackView(CreateView):
    model = FeedbackModel
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = reverse_lazy('done') # хардкод или лэйзи, просто реверс не успевает формировать ссылку


class DoneFeedbackView(TemplateView):
    template_name = 'feedback/done.html'
