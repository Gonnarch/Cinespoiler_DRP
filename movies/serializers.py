from rest_framework import serializers
from .models import Movie, Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = [
            "id",
            "name",
        ]
        read_only_fields = ['id']


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)

    genre_ids = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        many=True,
        write_only=True,
        source="genres",
        required=False
    )

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "slug",
            "description",
            "release_date",
            "duration_minutes",
            "image_url",
            "status",
            "genres",
            "genre_ids",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at"
        ]
