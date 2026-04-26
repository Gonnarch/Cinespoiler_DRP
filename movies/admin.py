from django.contrib import admin
from .models import Movie, Genre



@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "release_date", "duration_minutes")
    search_fields = ("title",)
    list_filter = ("genres",)
    filter_horizontal = ("genres",)  