from rest_framework import serializers
from blog.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    summary = serializers.CharField(required=False)
    class Meta:
        model = Movie
        fields = ['id', 'title', 'summary']
