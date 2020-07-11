from django.db import models
from django.utils import timezone


class EntryDate(models.Model):
    date = models.DateField()

# class Entry(models.Model):
#     value = models.IntegerField(default=0)
#     def __str__(self):
#        return str(self.date) + ':' + str(self.value)
# 
#     def __add__(self, other):
#         self.value = self.value + other.value
#     
#     def __int__(self):
#         return int(self.value)


