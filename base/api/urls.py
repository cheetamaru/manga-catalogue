from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ApiMangaListView.as_view()),
    path('getById/<str:pk>', views.getById.as_view()),
]
