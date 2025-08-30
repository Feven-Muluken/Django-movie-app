from django.contrib import admin
from .models import Movie, Gener
# Register your models here.

class GenerAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')

class MovieAdmin(admin.ModelAdmin):
  exclude = ('date_created',)
  list_display = ('number_in_stock', 'title', 'date_created', 'gener')

admin.site.register(Gener, GenerAdmin)
admin.site.register(Movie, MovieAdmin)