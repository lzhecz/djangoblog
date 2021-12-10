from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length = 255, verbose_name = 'Category name')
    slug = models.SlugField(max_length = 255, unique = True, db_index = True, verbose_name = "Category URL")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs = {'slug': self.slug})

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length = 50, verbose_name = 'Tag name')
    slug = models.SlugField(max_length = 50, unique = True, db_index = True, verbose_name = "Tag URL")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs = {'slug': self.slug})

    class Meta:
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length = 255, verbose_name = 'Post name', db_index = True)
    slug = models.SlugField(max_length = 255, unique = True, db_index = True, verbose_name = "Post URL")
    author = models.CharField(max_length = 255, verbose_name = 'Author name')
    content = models.TextField(blank = True, verbose_name = 'Post content')
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Creation time')
    photo = models.ImageField(blank = True, upload_to = "photos/%Y/%m/%d/", verbose_name = 'Photo')
    views = models.IntegerField(default = 0, verbose_name = 'Number of views')
    category = models.ForeignKey('Category', on_delete = models.PROTECT, verbose_name = 'Category',
                                 related_name = 'posts')
    tags = models.ManyToManyField('Tag', verbose_name = 'Tag')

    def get_absolute_url(self):
        return reverse('post', kwargs = {'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
