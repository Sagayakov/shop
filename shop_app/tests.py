from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import MarkModel, PhoneModel


class TestIndexView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('home')

        # Создаем две марки телефонов и несколько моделей каждой марки
        self.mark1 = MarkModel.objects.create(mark='Samsung', country='Корея', slug='samsung')
        self.mark2 = MarkModel.objects.create(mark='Apple', country='США', slug='apple')
        self.phone1 = PhoneModel.objects.create(mark_p=self.mark1, model_p='Galaxy S21', price_p=1000, slug='s21',
                                                is_public=True)
        self.phone2 = PhoneModel.objects.create(mark_p=self.mark1, model_p='Galaxy S20', price_p=800, slug='s20',
                                                is_public=True)
        self.phone3 = PhoneModel.objects.create(mark_p=self.mark2, model_p='iPhone 12', price_p=1200, slug='iphone-12',
                                                is_public=True)

    def test_index_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_index_pagination(self):
        response = self.client.get(self.url + '?page=1')

        # Проверяем, что пагинация работает корректно
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['phone']), 3)
        self.assertTemplateUsed(response, 'shop_app/index.html')
        self.assertEqual(response.context['page_obj'].number, 1)
        self.assertEqual(len(response.context['page_obj'].object_list), 3)

    def test_index_filter(self):
        # Создаем несколько моделей телефонов, которые не публикуются
        self.phone4 = PhoneModel.objects.create(mark_p=self.mark1, model_p='Galaxy S10', price_p=500, slug='s10',
                                                is_public=False)
        self.phone5 = PhoneModel.objects.create(mark_p=self.mark2, model_p='iPhone 11', price_p=1000, slug='iphone-11',
                                                is_public=False)

        response = self.client.get(self.url)

        # Проверяем, что модели телефонов отображаются только если они публикуются
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['phone']), 3)
        self.assertTemplateUsed(response, 'shop_app/index.html')
        self.assertNotIn(self.phone4, response.context['phone'])
        self.assertNotIn(self.phone5, response.context['phone'])


