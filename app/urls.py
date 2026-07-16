from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='app'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('status/', views.status_view, name='status'),
]

