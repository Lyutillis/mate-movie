from rest_framework import serializers
from django.db.models import

from movies.models import Movie, Genre, Star, Director


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"
