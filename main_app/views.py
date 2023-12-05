from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Computer
from django.urls import reverse_lazy



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
  success_url = reverse_lazy('index')

class ComputersUpdate(UpdateView):
    model = Computer
    fields = '__all__'
    template_name = 'main_app/computer_form.html'  # Replace with your actual template name
    success_url = reverse_lazy('index')  # Redirect to the computer list view

    def form_valid(self, form):
        print(form.errors)
        # Get the current object being edited
        self.object = self.get_object()

        # Update the existing instance with the form data
        form.instance = self.object

        # Save the form
        response = super().form_valid(form)

        return response

class ComputersDelete(DeleteView):
  model = Computer
  success_url = '/computers'