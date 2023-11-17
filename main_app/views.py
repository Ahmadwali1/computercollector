from django.shortcuts import render

# computers = [
#   {'name': 'macbook m2 14 inch', 'storage': '500 GB', 'Color': 'black', 'condition': 'new'},
#   {'name': 'macbook m3 16 inch', 'storage': '1 TB', 'Color': 'white', 'condition': 'old'},
# ]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def computers_index(request):
  return render(request, 'computers/index.html', {
    'computers': computers
  })
