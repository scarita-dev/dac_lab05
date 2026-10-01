from django.shortcuts import render
from django.db.models import Avg
from .models import Genre, Movie


def recommendations(request):
    selected_genre_id = request.GET.get('genre')
    genres = Genre.objects.all()

    movies = Movie.objects.annotate(
        avg_rating=Avg('ratings__score')
    ).filter(avg_rating__isnull=False)

    if selected_genre_id:
        movies = movies.filter(genres__id=selected_genre_id)

    movies = movies.order_by('-avg_rating')[:5]

    context = {
        'genres': genres,
        'movies': movies,
        'selected_genre_id': int(selected_genre_id) if selected_genre_id else None,
    }
    return render(request, 'movies/recommendations.html', context)