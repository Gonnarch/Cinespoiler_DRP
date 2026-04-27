from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'genres'
        ordering = ["name"]
        verbose_name = 'genre'
        verbose_name_plural = 'genres'

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    release_date = models.DateField(null=True, blank=True)
    duration_minutes = models.PositiveSmallIntegerField()
    image_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)

    genres = models.ManyToManyField(Genre, related_name="movies", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'movies'
        ordering = ['release_date']
        verbose_name = 'movie'
        verbose_name_plural = 'movies'

    def __str__(self):
        return self.title