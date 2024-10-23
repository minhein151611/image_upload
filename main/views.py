from django.shortcuts import render, redirect
from . models import *
from .forms import ImageForm

# Create your views here.

def index(request):
    images = Image.objects.all()
    context = {'images':images}
    return render(request, 'index.html', context)

def create(request):
    forms = ImageForm()
    if request.method == "POST":
        forms = ImageForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('index')
    context = {'forms':forms}
    return render(request, 'create.html', context)

def edit(request,pk):
    image = Image.objects.get(id=pk)
    forms=ImageForm(instance=image)
    if request.method == "POST":
        forms = ImageForm(request.POST, request.FILES, instance=image)
        if forms.is_valid():
            forms.save()
            return redirect('index')
    context = {'forms':forms}
    return render(request, 'edit.html', context)

def delete(request,pk):
    image = Image.objects.get(id=pk)
    if request.method == "POST":
        image.delete()
        return redirect('index')
    context = {'image':image}
    return render(request, 'delete.html', context)