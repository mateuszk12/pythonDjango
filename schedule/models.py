from django.utils import timezone

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name
class Task(models.Model):
    title = models.CharField(max_length=100,default="")
    description = models.CharField(max_length=500,default="")
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(Category,on_delete=models.RESTRICT)
    timestamp = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title