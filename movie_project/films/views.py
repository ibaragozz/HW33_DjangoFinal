# films/views.py

from django.shortcuts import render
from .models import Film  # Убедись, что у тебя есть модель Film

def home(request):
    return render(request, 'films/home.html')

def film_list(request):
    films = Film.objects.all()  # Убедись, что модель Film существует
    return render(request, 'films/film_list.html', {'films': films})

def add_film(request):
    return render(request, 'films/add_film.html')
