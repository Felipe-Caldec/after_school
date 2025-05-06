from django.shortcuts import render

def portada(request):
    return render(request, 'portada.html')

def talleres(request):
    return render(request, 'talleres.html')

def galeria(request):
    return render(request, 'galeria.html')