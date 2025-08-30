from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie
# Create your models here.
class MoviesResource(ModelResource):
  class Meta:
    queryset = Movie.objects.all()
    resource_name = 'movies'
    # excludes = ['release_year']