from django.db import models
from django.contrib.auth.models import User



class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
