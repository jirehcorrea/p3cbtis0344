from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index.html"),
    path("sucursal/", views.sucursal,name="sucursal.html"),
    path("cliente/", views.cliente,name="clientes.html"),
    path("producto/", views.producto,name="producto.html"),
    path("compra/", views.compra,name="compra.html"),
]