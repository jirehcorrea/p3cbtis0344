from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def sucursal(request):
    return render(request, "sucursal.html")

def cliente(request):
    return render(request, "cliente.html")

def producto(request):
    return render(request, "producto.html")

def compra(request):
    return render(request, "compra.html")