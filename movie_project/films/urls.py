from django.urls import path
from . import views  # Импорт представлений из текущей папки

urlpatterns = [
    path('', views.film_list, name='film_list'),  # Список фильмов
    path('add/', views.add_film, name='add_film'),  # Страница добавления фильма
]
