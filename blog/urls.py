from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<str:slug>/', PostByCategoryView.as_view(), name='category'),
    path('post/<str:slug>/', SinglePostView.as_view(), name='post'),
    path('tags/<str:slug>/', PostByTagsView.as_view(), name='tag'),
    path('search/', Search.as_view(), name='search'),
]
