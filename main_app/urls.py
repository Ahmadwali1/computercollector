from django.urls import path
from.import views


urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('computers/', views.computers_index, name='index'),
  path('computers/<int:computer_id>', views.computers_detail, name='detail'),
  path('computers/create/', views.ComputersCreate.as_view(), name='computers_create'),
]