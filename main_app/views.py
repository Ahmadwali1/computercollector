from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Computer
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
  comment_form = CommentForm()
  return render(request, 'computers/detail.html', {
    'computer': computer,
    'comment_form': comment_form
  })

class ComputersCreate(CreateView):
  model = Computer
  fields = '__all__'
  success_url = reverse_lazy('index')

class ComputersUpdate(UpdateView):
    model = Computer
    fields = '__all__'
    template_name = 'main_app/computer_form.html'  
    success_url = reverse_lazy('index')  

    def form_valid(self, form):
        print(form.errors)
        self.object = self.get_object()

        form.instance = self.object

        response = super().form_valid(form)

        return response

class ComputersDelete(DeleteView):
  model = Computer
  success_url = '/computers'