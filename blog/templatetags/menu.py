from django import template
from blog.models import Category

register = template.Library()


@register.inclusion_tag('blog/blogmenu.html')
def show_menu(menu_class='menu'):
    categories = Category.objects.all()
    return {'categories': categories, 'menu_class': menu_class}
