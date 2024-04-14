from django.urls import path, include
from rest_framework import routers

from . import views  # Substitua por .viewsets se for o caso

router = routers.DefaultRouter()
router.register('tarefas', views.TarefaViewSet)  # Substitua por views.TarefaViewSet se for o caso

urlpatterns = [
    path('', include(router.urls)),
]
