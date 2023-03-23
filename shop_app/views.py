from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *


class IndexView(ListView):
    """Вывод объектов на главную страницу"""

    paginate_by = 6
    model = PhoneModel
    template_name = 'shop_app/index.html'
    context_object_name = 'phone'
    extra_context = {
        'title': 'Главная страница',
        'main_word': 'Все модели телефонов'
    }

    def get_queryset(self):
        """Фильтрует выдаваемые объекты моделей"""
        return PhoneModel.objects.filter(is_public=True).select_related('mark_p')


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
    """Вывод одной модели телефона"""

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
    """Сортированный вывод объектов по первичной модели"""

    paginate_by = 4
    model = PhoneModel
    template_name = 'shop_app/index.html'
    context_object_name = 'phone'
    allow_empty = False  # если список пуст, выводит 404

    def get_queryset(self):
        return PhoneModel.objects.filter(mark_p__slug=self.kwargs['mark_slug'], is_public=True).select_related('mark_p')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        name_model = context["phone"][0].mark_p
        context['main_word'] = f'Все модели {name_model}'
        context['title'] = f'Телефоны {name_model}'
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

class RegisterUser(CreateView):
    """Регистрация пользователя"""

    form_class = RegisterForm
    template_name = 'shop_app/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        """Автоматическая авторизация пользователя после регистрации"""

        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    """Авторизация пользователя"""

    form_class = LoginForm
    template_name = 'shop_app/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    """Выход пользователя"""

    logout(request)
    return redirect('login')
