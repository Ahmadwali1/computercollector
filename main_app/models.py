from django.db import models
from django.urls import reverse



class Computer(models.Model):
  name = models.CharField(max_length=200)
  storage = models.CharField(max_length=100)
  Color = models.CharField(max_length=100)
  condition = models.CharField(max_length=100)

def __str__(self):
  return f'{self.name} ({self.id})'

def get_absolute_url(self):
  return reverse('detail', kwargs={'computer_id': self.id})

