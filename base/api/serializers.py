from rest_framework.serializers import ModelSerializer
from base.models import MangaTitle

class MangaTitleSerializer(ModelSerializer):
    class Meta:
        model = MangaTitle
        fields = '__all__'