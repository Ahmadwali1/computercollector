from django.urls import path
from.import views


urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('computers/', views.computers_index, name='index'),
  path('computers/<int:computer_id>', views.computers_detail, name='detail'),
  path('computers/create/', views.ComputersCreate.as_view(), name='computers_create'),
  path('computers/<int:pk>/update/', views.ComputersUpdate.as_view(), name='computers_update'),
  path('computers/<int:pk>/delete/', views.ComputersDelete.as_view(), name='computers_delete'),
]