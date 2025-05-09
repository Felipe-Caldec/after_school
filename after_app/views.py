from django.shortcuts import render, redirect
from django.core.mail import send_mail

def portada(request):

    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        correo = request.POST.get("correo")
        telefono = request.POST.get("telefono")
        mensaje = request.POST.get("mensaje")
        fecha = request.POST.get("fecha")

        asunto = "Nuevo mensaje de contacto"
        cuerpo = (
            f"Nombre: {nombre} {apellido}\n"
            f"Correo: {correo}\n"
            f"Teléfono: {telefono}\n"
            f"Fecha: {fecha}\n"
            f"Mensaje:\n{mensaje}"
        )
        send_mail(asunto, cuerpo, correo, ['felipe.betocalderon@gmail.com'])
        return redirect("{% url 'portada' %}")
    
    return render(request, 'portada.html')

def talleres(request):
    return render(request, 'talleres.html')

def galeria(request):
    return render(request, 'galeria.html')

def quienes_somos(request):
    return render(request, 'quienes_somos.html')