from django.db import models

# Create your models here.
#computers = [
#   {'name': 'macbook m2 14 inch', 'storage': '500 GB', 'Color': 'black', 'condition': 'new'},
#   {'name': 'macbook m3 16 inch', 'storage': '1 TB', 'Color': 'white', 'condition': 'old'},
# ]
class Computer(models.Model):
  name = models.CharField(max_length=200)
  storage = models.CharField(max_length=100)
  Color = models.CharField(max_length=100)
  condition = models.CharField(max_length=100)
