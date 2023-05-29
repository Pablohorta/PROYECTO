from django.shortcuts import render, redirect
from . import forms

def index (request):
    return render (request, "home/index.html")

def crear_cita (request):
    if request.method == "POST":
        form = forms.cita_agendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect (request, "home:index")
    else:    
        form = forms.cita_agendaForm()
        context = {"form": form}
        return render (request, "home/crear_cita.html", context)
    
    
    
def crear_autor (request):
    if request.method == "POST":
        form = forms.autorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect (request, "home:index")
    else:    
        form = forms.autorForm()
        context = {"form": form}
        return render (request, "home/crear_autor.html", context)


def crear_cliente (request):
    if request.method == "POST":
        form = forms.clienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect (request, "home:index")
    else:    
        form = forms.clienteForm()
        context = {"form": form}
        return render (request, "home/crear_autor.html", context)

