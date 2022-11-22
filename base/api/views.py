from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from base.models import MangaTitle
from .serializers import MangaTitleSerializer

class getById(RetrieveAPIView):
    queryset=MangaTitle.objects.all()
    serializer_class = MangaTitleSerializer

class ApiMangaListView(ListAPIView):
    queryset = MangaTitle.objects.all()
    serializer_class = MangaTitleSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('name', 'description')
    filterset_fields = ('authors', 'genres', 'status')
