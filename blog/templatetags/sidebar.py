from django import template
from blog.models import Post, Tag

register = template.Library()


@register.inclusion_tag('blog/popular.html')
def get_popular_post(cnt=None):
    posts = Post.objects.order_by('-views')[:cnt]
    return {'posts': posts}


@register.inclusion_tag('blog/tags_cloud.html')
def get_tags_cloud(cnt=None):
    tags = Tag.objects.all()[:cnt]
    return {'tags': tags}
