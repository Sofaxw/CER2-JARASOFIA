from django.shortcuts import render
from django.http import HttpResponse
from .models import Comunicado, Entidad

# Create your views here.
def inicio(request):

    title = "Inicio"
    entity = Entidad.objects.all()
    comunicados= Comunicado.objects.all()
    

    data = {
        "title": title,
        "entity": entity,
        "comunicados": comunicados,
    }

    return render(request, 'miapp/index.html', data)



def filtrar(request):
    departamento = request.GET.get('depto')

    comunicados = Comunicado.objects.filter(entidad__nombre=departamento).order_by('-fecha_publicacion') if departamento != "Todos" else Comunicado.objects.all().order_by('-fecha_publicacion')

    entity = Entidad.objects.all().order_by('nombre')

    data = {
        "comunicados": comunicados,
        "entity": entity,
    }

    return render(request, 'miapp/index.html', data)

