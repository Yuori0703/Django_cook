from django import template
from cook.models import Category
from django.db.models import Count
from django.db.models import Q
from django.core.cache import cache


register = template.Library()



# @register.simple_tag
# def get_all_categories():
#     return Category.objects.annotate(
#         cnt=Count('post', filter=Q(post__is_published=True))
#     ).filter(cnt__gt=0)

@register.simple_tag
def get_all_categories():
    buttons = cache.get('category')
    
    if not buttons:
        buttons = Category.objects.annotate(cnt=Count('post', filter=Q(post__is_published=True))).filter(cnt__gt=0)
        cache.set('category', buttons, 60)

    return buttons
    