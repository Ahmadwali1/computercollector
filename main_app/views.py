from django.shortcuts import render
from django.views.generic.edit import CreateView
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

def computers_detail(request, computer_id):
  computers = Computer.objects.get(id = computer_id)
  return render(request, 'computers/detail.html', {
    'computers': computers
  })

class ComputerCreate(CreateView):
  model = Computer
  fields = '__all__'

