from django.shortcuts import render, redirect
from .models import Posts, User, Comentarios

# Create your views here.

# vista basada en funciones
def posts(request):
    ctx = {}  # contextos/ diccionarios CONSULTAR
    noticias = Posts.objects.all()  # select * from Posts
    ctx["noticias"] = noticias
    # print(noticias)
    return render(request, "posts/posts.html", ctx)


def about_us(request):
    return render(request, "posts/about_us.html")

def registro(request):
    return render(request,"usuarios/registro.html")

# vistas badas en clases

from .form import RegistroForm
from django.views.generic import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

#Creamos el formulario(form.py) y acá lo renderizamos donde queremos que aparezca

class Registro(CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy("noticias")
    template_name = "usuarios/registro.html"