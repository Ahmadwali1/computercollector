from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
  computer = Computer.objects.get(id = computer_id)
  return render(request, 'computers/detail.html', {
    'computer': computer
  })

class ComputersCreate(CreateView):
  model = Computer
  fields = '__all__'
  success_url = '/computers/{computer_id}'

class ComputersUpdate(UpdateView):
  model = Computer
  # fields = ['Condition', 'Storage', 'Color']
  fields = '__all__'

class ComputersDelete(DeleteView):
  model = Computer
  success_url = '/computers'