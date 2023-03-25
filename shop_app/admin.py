from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import MarkModel, PhoneModel


# Register your models here.

# admin.site.register(MarkModel)
# admin.site.register(PhoneModel)


@admin.register(PhoneModel)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_photo', 'mark_p', 'model_p', 'price_p', 'new_price', 'is_public']
    list_display_links = ['mark_p', 'model_p', 'get_photo']
    search_fields = ['model_p']
    list_editable = ['is_public']
    fields = ['mark_p', 'model_p', 'description', 'price_p', 'discount_p',
              'new_price', 'slug', 'photo', 'get_photo',  'is_public',
              'date_create', 'date_update']
    readonly_fields = ['date_create', 'date_update', 'new_price', 'get_photo']

    @admin.display(ordering='price_p', description='new_price')
    def new_price(self, ph: PhoneModel):
        if ph.discount_p:
            return f'{ph.price_p - ph.discount_p}'
        return ph.price_p

    def get_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width=70>')

    get_photo.short_description = 'Фото'
    new_price.short_description = 'Цена со скидкой'


@admin.register(MarkModel)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'mark', 'country')
    list_display_links = ('id', 'mark')
    search_fields = ('mark',)
    prepopulated_fields = {'slug': ('mark',)}


admin.site.site_header = 'Админ панель сайта Shop'
admin.site.site_title = 'Shop'
