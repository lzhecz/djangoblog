from django.urls import path

from .views import *

urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('category/<str:slug>/', PostByCat.as_view(), name = 'category'),
    path('tag/<str:slug>/', PostByTag.as_view(), name = 'tag'),
    path('post/<str:slug>/', PostView.as_view(), name = 'post'),
]
