from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('list/', views.getList),
    path('getById/<str:pk>', views.getById),
]
