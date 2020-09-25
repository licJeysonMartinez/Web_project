from django.shortcuts import render,redirect
from .models import Reservar
from.form import reservaform

def inicio(request):
    return render(request, 'index.html')

def informacion(request):
    return render(request, 'info.html')

def ver_reserva(request):
    reservas = Reservar.objects.all()
    contexto =  {'reservas': reservas
    }
    return render(request, 'reserva.html',contexto)

def reservar(request):
    if request.method == "GET":
        form = reservaform()
        contexto = {
            'form': form
        }
    else:
        form = reservaform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('ver_reserva')     
    return render(request, 'reserva_form.html',{'form':form})   


def editar(request,id):
    reservas = Reservar.objects.get(id = id)
    if request.method == "GET":
        form = reservaform(instance = reservas)
        contexto = {
            'form':form

        }
    else:
        form = reservaform(request.POST, instance = reservas)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('ver_reserva')
    return render(request,'reserva_form.html',contexto)

def eliminar(request,id):
    reservas = Reservar.objects.get(id = id)
    reservas.delete()
    return redirect('ver_reserva')

