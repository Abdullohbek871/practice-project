from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Task(models.Model):
    STATUS_CHOICES = (
        ('cp', 'Completed'),
        ('ip', 'In Progress'),
        ('fl', 'Failed'),
    )
    title = models.CharField(max_length=100)
    due_date = models.DateTimeField()
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title

class Todo(models.Model):
    pass



