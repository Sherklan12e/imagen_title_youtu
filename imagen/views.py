from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm
from django.shortcuts import get_object_or_404 


def index(request):
    if request.method== 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    else:
        form = ImageForm()
    imagenes = Image.objects.all()
    return render(request, 'index.html', {'form':form, 'imagenes':imagenes})


def eliminar(request, idimagen):
    imagen = get_object_or_404(Image ,pk=idimagen)
    imagen.delete()
    return redirect('index')