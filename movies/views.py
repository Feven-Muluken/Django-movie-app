from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import  Movie


def index(request):
  movies = Movie.objects.all()
  # output = ', '.join([m.title for m in movies])
  # # SELECT * FROM movies_movie
  # Movie.objects.filter(release_year=1984)
  # # SELECT * FROM movies_movie WHERE release_year=1984
  # Movie.objects.get(id=1)
  # return HttpResponse(output)
  return render(request, 'movies/index.html', {'movies': movies})

def detail(request, movie_id):
  movie = get_object_or_404(Movie ,id=movie_id)
  return render(request, 'movies/detail.html', {'movie': movie})

   