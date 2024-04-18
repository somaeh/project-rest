
from rest_framework import serializers
from .models import Todo
from .models import User



class Todoserializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields =['title', 'content', 'user']
        
class  Userserializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']