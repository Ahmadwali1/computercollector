from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Computer, Accessory
from django.urls import reverse_lazy
from .forms import CommentForm



# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def computers_index(request):
  computers = Computer.objects.all()
  return render(request, 'computers/index.html', {
    'computers': computers,
  })

def computers_detail(request, computer_id):
  computer = Computer.objects.get(id = computer_id)
  id_list = computer.accessories.all().values_list('id')
  accessories_computer_doesnt_have = Accessory.objects.exclude(id__in=id_list)
  comment_form = CommentForm()
  return render(request, 'computers/detail.html', {
    'computer': computer,
    'comment_form': comment_form,
    'accessories': accessories_computer_doesnt_have
  })

class ComputersCreate(CreateView):
  model = Computer
  fields = ['name','storage','color','condition']
  success_url = reverse_lazy('index')

class ComputersUpdate(UpdateView):
    model = Computer
    fields = ['name','storage','color','condition']
    template_name = 'main_app/computer_form.html'  
    success_url = reverse_lazy('index')  


class ComputersDelete(DeleteView):
  model = Computer
  success_url = '/computers'


def add_comment(request, computer_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.computer_id = computer_id
        new_comment.save()
    return redirect('detail', computer_id=computer_id)

def accessories_index(request):
  accessories = Accessory.objects.all()
  return render(request, 'computers/accessory.html', {
    'accessories': accessories,
  })

class AccessoriesCreate(CreateView):
  model = Accessory
  fields = '__all__'
  success_url = reverse_lazy('accessory')

class AccessoriesDelete(DeleteView):
  model = Accessory
  success_url = '/accessories'

def accessories(request, computer_id, accessory_id):
  Computer.objects.get(id=computer_id).accessories.add(accessory_id)
  return redirect('detail', computer_id=computer_id)