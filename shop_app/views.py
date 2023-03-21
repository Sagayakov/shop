from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import *


class IndexView(ListView):
    model = PhoneModel
    template_name = 'shop_app/index.html'
    context_object_name = 'phone'
    extra_context = {
        'title': 'Главная страница',
        'main_word': 'Все модели телефонов'
    }

    def get_queryset(self):
        """Фильтрует выдаваемые объекты моделей"""
        return PhoneModel.objects.filter(is_public=True)

# def index(request):
#     phone = PhoneModel.objects.all()
#
#     context = {
#         'phone': phone,
#         'main_word': 'Все модели телефонов',
#         'title': 'Главная страница'
#     }
#
#     return render(request, 'shop_app/index.html', context=context)


class PhoneView(DetailView):
    model = PhoneModel
    template_name = 'shop_app/phone.html'
    slug_url_kwarg = 'phone_slug'
    context_object_name = 'phone'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"{context['phone'].mark_p} {context['phone'].model_p.upper()}"
        return context


# def show_phone(request, phone_slug):
#     phone = get_object_or_404(PhoneModel, slug=phone_slug)
#
#     context = {
#         'phone': phone,
#         'title': f'{phone.mark_p} {phone.model_p.upper()}'
#     }
#     return render(request, 'shop_app/phone.html', context=context)


class MarkView(ListView):
    model = PhoneModel
    template_name = 'shop_app/index.html'
    context_object_name = 'phone'
    allow_empty = False # если список пуст, выводит 404

    def get_queryset(self):
        return PhoneModel.objects.filter(mark_p__slug=self.kwargs['mark_slug'], is_public=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_word'] = f'Все модели {self.get_queryset()[0].mark_p}'
        context['title'] = f'Телефоны {context["phone"][0].mark_p}' # наверное этот вариант более быстрый, нет вызова функции
        return context


# def show_mark(request, mark_slug):
#     phone = PhoneModel.objects.filter(mark_p__slug=mark_slug)
#
#     context = {
#         'phone': phone,
#         'main_word': f'Все модели {phone[0].mark_p}',
#         'title': f'Телефоны {phone[0].mark_p}'
#     }
#     return render(request, 'shop_app/index.html', context=context)
