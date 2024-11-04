# films/views.py

from django.shortcuts import render, redirect
from .models import Film
from .forms import FilmForm

def home(request):
    return render(request, 'films/home.html')

def film_list(request):
    films = Film.objects.all()  # Убедись, что модель Film существует
    return render(request, 'films/film_list.html', {'films': films})


def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправление на главную страницу или другую страницу после сохранения
    else:
        form = FilmForm()

    return render(request, 'films/add_film.html', {'form': form})
