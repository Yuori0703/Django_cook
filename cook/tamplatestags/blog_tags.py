from django import template
from cook.models import Category


register = template.Library()

# new*
@register.simple_tag()
def get_all_categories():
    # Кнопки категорий
    return Category.objects.all()