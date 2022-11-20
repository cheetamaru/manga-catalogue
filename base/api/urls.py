from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('list/', views.ApiMangaListView.as_view()),
    path('getById/<str:pk>', views.getById),
]
