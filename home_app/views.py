from django.shortcuts import render
from todo_app.models import Todo



def index(request):
    todo = Todo.objects.all()
    return render(request, 'home_app/index.html', context={'todo': todo})
