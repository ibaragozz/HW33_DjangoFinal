from django.shortcuts import render, redirect
from .models import Film
from .forms import FilmForm

# Страница для добавления фильма
def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('film_list')
    else:
        form = FilmForm()
    return render(request, 'add_film.html', {'form': form})

# Страница для просмотра фильмов
def film_list(request):
    films = Film.objects.all()
    return render(request, 'film_list.html', {'films': films})

