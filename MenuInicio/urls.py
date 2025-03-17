from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear/', views.crear_post, name='crear_post'),
    path('buscar/', views.buscar, name='buscar'),
    path('listar/', views.listar_posts, name='listar_posts'),
]
