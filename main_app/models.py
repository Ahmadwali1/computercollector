from django.db import models
from django.urls import reverse


class Accessory(models.Model):
  name = models.CharField(max_length=200)
  color = models.CharField(max_length=100)
  condition = models.CharField(max_length=100)

  def __str__(self):
    return f"{self.name} - {self.color} ({self.condition})"







class Computer(models.Model):
  name = models.CharField(max_length=200)
  storage = models.CharField(max_length=100)
  color = models.CharField(max_length=100)
  condition = models.CharField(max_length=100)

  # accessories = models.ManyToManyField(accessory)

def __str__(self):
  return f'{self.name} ({self.id})'

def get_absolute_url(self):
  return reverse('detail', args=[str(self.id)])



class Comment(models.Model):
  date= models.DateField(auto_now_add=True)
  review = models.CharField(max_length=5000)

  computer = models.ForeignKey(Computer, on_delete=models.CASCADE,blank=True, null=True)

  def __str__(self):
    return f"{self.date} - {self.review}"


