from django import template
from blog.models import Category
from django.db.models import F, Count

register = template.Library()


@register.inclusion_tag('blog/menu_tpl.html')
def show_menu(menu_class='menu'):
    # categories = Category.objects.annotate(cnt=Count("posts", filter=F('posts__is_published')))
    categories = Category.objects.all()
    return {'categories': categories, 'menu_class': menu_class}
