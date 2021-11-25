from django.urls import reverse_lazy
from django.views.generic import CreateView
from todo.models import Task


class TaskView(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'todo/todo.html'
    # success_url = reverse_lazy('todo:')
