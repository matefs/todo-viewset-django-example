
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')),  # Inclua as URLs do aplicativo "todo"


]
