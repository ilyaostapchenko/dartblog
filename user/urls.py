from django.urls import path

from .views import *

urlpatterns = [
    path('genres/', rubric, name='rubric'),
    path('genres/<int:pk>/', happy_rubric, name='happy_rubric'),
]
