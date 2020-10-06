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
    path('<int:produto_id>/', views.produto, name="produto"),
    path('buscar', views.busca, name='buscar'),
    path('sobre/', views.sobre, name='sobre'),
    path('carrinho/', views.carrinho, name='carrinho')
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
