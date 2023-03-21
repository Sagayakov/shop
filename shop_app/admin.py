from django.contrib import admin
from .models import MarkModel, PhoneModel

# Register your models here.

# admin.site.register(MarkModel)
# admin.site.register(PhoneModel)


@admin.register(PhoneModel)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'mark_p', 'model_p', 'price_p', 'new_price', 'is_public']
    list_display_links = ['mark_p', 'model_p']
    search_fields = ['model_p']
    list_editable = ['is_public']

    @admin.display(ordering='price_p', description='new_price')
    def new_price(self, ph: PhoneModel):
        if ph.discount_p:
            return f'{ph.price_p - ph.discount_p}'


@admin.register(MarkModel)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'mark', 'country')
    list_display_links = ('id', 'mark')
    search_fields = ('mark', )
    prepopulated_fields = {'slug': ('mark',)}
