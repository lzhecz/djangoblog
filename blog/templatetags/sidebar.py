from django import template
from blog.models import Post, Tag

register = template.Library()


@register.inclusion_tag('blog/popular.html')
def get_popular_post(cnt=3):
    posts = Post.objects.order_by('-views')[:cnt]
    return {'posts': posts}
