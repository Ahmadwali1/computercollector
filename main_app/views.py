from django.shortcuts import render
from .models import Computer


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def computers_index(request):
  computers = Computer.objects.all()
  return render(request, 'computers/index.html', {
    'computers': computers
  })
