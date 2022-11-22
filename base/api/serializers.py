from rest_framework.serializers import ModelSerializer
from base.models import MangaTitle, MangaAuthor, Genre

class MangaAuthorSerializer(ModelSerializer):
    class Meta:
        model = MangaAuthor
        fields = '__all__'

class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MangaTitleSerializer(ModelSerializer):
    authors = MangaAuthorSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = MangaTitle
        fields = '__all__'