from django.shortcuts import render
from . models import *

# Create your views here.

def index(request):
    images = Image.objects.all()
    context = {'images':images}
    return render(request, 'index.html', context)