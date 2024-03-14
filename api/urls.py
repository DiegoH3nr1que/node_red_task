from django.urls import path
from api.views import DadosViewSet

# Definir manualmente as rotas para cada ação do ViewSet
urlpatterns = [
    path('api/dados/', DadosViewSet.as_view({'get': 'list', 'post': 'create'}), name='dados-list'),
    path('api/dados/<int:pk>/', DadosViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='dados-detail'),
]
