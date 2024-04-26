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
from rest_framework.views import APIView 
from rest_framework import generics, mixins
from rest_framework import viewsets
from django.contrib.auth import get_user_model

user = get_user_model()


#region function base view
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
        return Response(serializer2.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response("you only use get or post", status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def all_user(request: Request):
    users = User.objects.all()
    serializer = Userserializers(users, many=True)
    return Response(serializer.data, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def todo_details_view(request: Request, todo_id:int):
    try:
        todo = Todo.objects.get(pk=todo_id)
    except todo.DoesNotExist:
        return Response("not found", status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = Todoserializers(todo)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer_put = Todoserializers(todo, data=request.data)
        if serializer_put.is_valid():
            serializer_put.save()
            return Response(serializer_put.data, status.HTTP_202_ACCEPTED)
        return Response(serializer_put.errors, status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        todo.delete()
        return Response("not found", status.HTTP_404_NOT_FOUND)
   

    
    
    
        

    


#region class base view

class TodosListApiview(APIView):
    def get(self, request: Request):
      todos = Todo.objects.all()
      serializer1 = Todoserializers(todos, many=True)
      return Response(serializer1.data, status.HTTP_200_OK)
    def post(self, request: Request):
        serializer2 = Todoserializers(data=request.data)
        if serializer2.is_valid():
            serializer2.save()
            return Response(serializer2.data, status.HTTP_201_CREATED)
        else:
            return Response("not fpund", status.HTTP_400_BAD_REQUEST)
class TodosDetailApiview(APIView):
    
    def get_object(self, todo_id: int):
        try:
            todo = Todo.objects.get(pk=todo_id)
            return todo
        except todo.DoesNotExist:
            return Response("not found", status.HTTP_404_NOT_FOUND)
            
        
    
    def get(self, request: Request, todo_id: int):
        todo = self.get_object(todo_id)
        serializer = Todoserializers(todo)
        return Response(serializer.data, status.HTTP_200_OK)
        
        
      
            
    
    def put(self, request: Request, todo_id: int):
        todo = self.get_object(todo_id)
        serializer_put = Todoserializers(todo, data=request.data)
        if serializer_put.is_valid():
            serializer_put.save()
            return Response(serializer_put.data, status.HTTP_202_ACCEPTED)
        return Response("ddd", status.HTTP_400_BAD_REQUEST)
                                           
      
    def delete(self, request: Request, todo_id: int):
         todo = self.get_object(todo_id)
         todo.delete()
         return Response("not found", status.HTTP_404_NOT_FOUND)
          
#endregion


#region mixins
class TodosListMixinsApiview(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = Todoserializers
    
    def get(self, request: Request):
        return self.list(request)
    def post(self, request: Request):
        return self.create(request)
    
    
class TodosDetailMixinsApiview(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = Todoserializers
    
    def get(self, request: Request, pk):
        return self.retrieve(request, pk)
    def put(self, request: Request, pk):
        return self.update(request, pk)
    def delete(self, request: Request, pk):
        return self.destroy(request, pk)

    


#endregion
#region generics
class TodoGenericApiview(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = Todoserializers
    
class TodoGenericDtailApiview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = Todoserializers

    
#endregion
#region viewset

class TodoViewApiview(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = Todoserializers

#endregion
#region user

class UsersGenericApiview(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class =  Userserializers
    

#endregion


    
    
    
    