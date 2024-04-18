from django.shortcuts import render
from todo_app.models import Todo
from django.http import HttpRequest, JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view



def index(request):
    todo = Todo.objects.all()
    return render(request, 'home_app/index.html', context={'todo': todo})

@api_view(['GET'])
def todos_json(request: Request): 
    todos = list( Todo.objects.all().values('title', 'is_done'))
    return Response({'todos': todos}, status.HTTP_200_OK)
