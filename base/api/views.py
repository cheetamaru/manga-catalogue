from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
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
def getList(request):
    try:
        list = MangaTitle.objects.all()
    except MangaTitle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MangaTitleSerializer(list, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getById(request, pk):
    try:
        item = MangaTitle.objects.get(id=pk)
    except MangaTitle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MangaTitleSerializer(item, many=False)
        return Response(serializer.data)