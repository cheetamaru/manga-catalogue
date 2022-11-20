from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from base.models import MangaTitle
from .serializers import MangaTitleSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/list',
        'GET /api/getById/:id'
    ]
    return Response(routes)

@api_view(['GET'])
def getById(request, pk):
    try:
        item = MangaTitle.objects.get(id=pk)
    except MangaTitle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MangaTitleSerializer(item, many=False)
        return Response(serializer.data)

class ApiMangaListView(ListAPIView):
    queryset = MangaTitle.objects.all()
    serializer_class = MangaTitleSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'description')
