from django.shortcuts import render

from .models import Todo
from .models import User
from .serializers import Todoserializers
from .serializers import Userserializers
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET'])
def all_todo(request: Request):
    todos = Todo.objects.all()
    serializer = Todoserializers(todos, many=True)
    return Response(serializer.data, status.HTTP_200_OK)

@api_view(['GET'])
def all_user(request: Request):
    users = User.objects.all()
    serializer = Userserializers(users, many=True)
    return Response(serializer.data, status.HTTP_200_OK)