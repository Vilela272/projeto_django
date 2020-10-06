from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:categoria_id>/', views.categoria, name="categoria")
] 
