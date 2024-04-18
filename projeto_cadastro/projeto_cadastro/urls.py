from django.urls import path, include
from app_cadastro import views
from rest_framework.routers import DefaultRouter
from app_cadastro.views import UsuarioViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('adicionar/', views.adicionar_usuario, name='adicionar_usuario'),
    path('usuarios/', views.listagem_usuarios, name='listagem_usuarios'),
    path('editar/<int:id_usuario>/', views.editar_usuario, name='editar_usuario'),
    path('excluir/<int:id_usuario>/', views.excluir_usuario, name='excluir_usuario'),
    path('check-nome/', views.check_nome, name='check-nome'),
    path('api/', include(router.urls)),  # Mover a URL da API para cá
]
