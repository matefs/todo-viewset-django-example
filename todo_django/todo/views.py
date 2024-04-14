from django.urls import path, include
from rest_framework import routers
from .viewsets import TarefaViewSet

router = routers.DefaultRouter()
router.register('tarefas', TarefaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
