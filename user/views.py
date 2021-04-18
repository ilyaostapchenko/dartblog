from django.shortcuts import render

from .models import Rubric

def rubric(request):
    return render(request, 'user/templatetest.html', {'rubrics': Rubric.objects.all()})

def happy_rubric(request):
    pass