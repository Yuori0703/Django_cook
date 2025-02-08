from django import template
from cook.models import Category
from django.db.models import Count
from django.db.models import Q


register = template.Library()

@register.simple_tag()
def get_all_categories():
    return Category.objects.annotate(cnt=Count('post')).filter(Q(posts__is_published=True) & Q(cnt__gt=0))
