from django.db import models



class Computer(models.Model):
  name = models.CharField(max_length=200)
  storage = models.CharField(max_length=100)
  Color = models.CharField(max_length=100)
  condition = models.CharField(max_length=100)

