from django.shortcuts import render

from .models import Todo
from .models import User
from .serializers import Todoserializers
from .serializers import Userserializers
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser



@api_view(['GET', 'POST'])
def all_todo(request: Request):
   if request.method == 'GET':
        todos = Todo.objects.all()
        serializer1 = Todoserializers(todos, many=True)
        return Response(serializer1.data, status.HTTP_200_OK)
   elif request.method == 'POST':
       serializer2 = Todoserializers(data=request.data)
       if serializer2.is_valid():
           serializer2.save()
           return Response(serializer2.data, status.HTTP_201_CREATED)
   return Response(None, status.HTTP_200_OK)

@api_view(['GET'])
def all_user(request: Request):
    users = User.objects.all()
    serializer = Userserializers(users, many=True)
    return Response(serializer.data, status.HTTP_400_BAD_REQUEST)