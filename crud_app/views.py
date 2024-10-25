from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = 'dashboard.html'
    context_object_name = 'todos'

    def get_queryset(self):
      return Task.objects.filter(user=self.request.user)

class TaskCreateView(CreateView):
    model = Task
    template_name = 'create-task.html'
    fields = ['title', 'description', 'due_date']

    def get_success_url(self):
        return reverse_lazy('app_name:todo-list')

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'edit-task.html'
    fields = ['title', 'description', 'due_date']

    def get_success_url(self):
        return reverse_lazy('app_name:todo-list')

class TaskDeleteView(DeleteView):
    model = Task


    def get_success_url(self):
        return reverse_lazy('app_name:todo-list')

