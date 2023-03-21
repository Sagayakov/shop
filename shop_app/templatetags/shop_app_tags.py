from django import template
from shop_app.models import *

register = template.Library()


@register.simple_tag()
def get_marks():
    return MarkModel.objects.all()
