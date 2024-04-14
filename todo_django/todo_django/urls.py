
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


from todo.viewsets import TarefaViewSet


router = routers.DefaultRouter()
router.register('tarefas', TarefaViewSet)  # Substitua por views.TarefaViewSet se for o caso

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

]
