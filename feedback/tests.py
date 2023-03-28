from django.test import TestCase
from django.urls import reverse

from .models import FeedbackModel
from .forms import FeedbackForm


class FeedbackViewTestCase(TestCase):
    def test_feedback_view_form_submission(self):
        # Подготавливаем данные формы
        form_data = {
            'name': 'Test User',
            'surname': 'Test',
            'rating': '7',
            'feedback': 'Test message'
        }

        # Отправляем POST-запрос с данными формы на обработку
        response = self.client.post(reverse('feedback'), form_data)

        # Проверяем, что форма была успешно отправлена и произошел редирект на страницу "done"
        self.assertEqual(response.status_code, 302)
        # self.assertRedirects(response, reverse('done'))

        # Проверяем, что объект модели был создан в базе данных с указанными данными
        feedback_test = FeedbackModel.objects.get(surname='Test')
        self.assertEqual(feedback_test.name, 'Test User')
        self.assertEqual(feedback_test.feedback, 'Test message')
        self.assertEqual(feedback_test.rating, 7)

    def test_feedback_view_form_display(self):
        # Отправляем GET-запрос на страницу с формой обратной связи
        response = self.client.get(reverse('feedback'))

        # Проверяем, что страница содержит форму обратной связи
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<form')
        self.assertIsInstance(response.context['form'], FeedbackForm)


class DoneFeedbackViewTestCase(TestCase):
    def test_done_feedback_view_display(self):
        # Отправляем GET-запрос на страницу с сообщением об успешной отправке формы обратной связи
        response = self.client.get(reverse('done'))

        # Проверяем, что страница отображается корректно
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Отзыв успешно принят')
