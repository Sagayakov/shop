from django.contrib import admin
from .models import FeedbackModel
from django.db.models import QuerySet


# Register your models here.


class RatingFilter(admin.SimpleListFilter):
    """Класс устанавливающий параметры фильтрации"""

    title = 'Filter list'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<3', 'Очень низкий'),
            ('3-4', 'Низкий'),
            ('5-7', 'Хороший'),
            ('7>', 'Высокий')
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<3':
            return queryset.filter(rating__lte=3)
        elif self.value() == '3-5':
            return queryset.filter(rating__lt=6)
        elif self.value() == '6-7':
            return queryset.filter(rating__lte=7)
        elif self.value() == '7>':
            return queryset.filter(rating__gt=7)
        return


@admin.register(FeedbackModel)
class FeedbackAdmin(admin.ModelAdmin):
    """Класс отвечающий за отображание админки"""

    list_display = ['id', 'name', 'surname', 'sex', 'rating', 'rating_status']
    search_fields = ['name__startswith']
    list_filter = [RatingFilter, 'name']

    @admin.display(ordering='rating', description='Status')
    def rating_status(self, feed: FeedbackModel):
        """Выводит текстовое описание рейтинга в list_display. Новый столбец"""

        if feed.rating <= 3:
            return 'Очень низкий'
        elif 3 < feed.rating <= 5:
            return "Низкий"
        elif 5 < feed.rating <= 7:
            return "Хороший"
        return 'Высокий'
