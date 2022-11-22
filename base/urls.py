from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

schema_view = swagger_get_schema_view(
    openapi.Info(
        title='Manga Catalogue API',
        default_version="1.0.0"
    ),
    public=True,
)

urlpatterns = [
    path('api/',
    include([
        path('', include('base.api.urls')),
        path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema')
    ]))
    
]
