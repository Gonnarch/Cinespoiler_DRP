from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=150)
    synopsis = models.TextField(blank=True)
    duration_minutes = models.PositiveIntegerField()
    release_date = models.DateField()
    is_showing = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self) -> str:
        return self.title