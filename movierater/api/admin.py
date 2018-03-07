from django.contrib import admin
from movierater.api.models import Movie, Rating

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = ('title', 'description')
    list_display = ['title', 'description']
    search_fields = ('title', 'description')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    fields = ('user', 'movie', 'stars')
    list_display = ['user', 'movie', 'stars']
    search_fields = ('movie',)

