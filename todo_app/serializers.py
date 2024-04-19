
from rest_framework import serializers
from .models import Todo
from .models import User



class Todoserializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
        
        
class  Userserializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields ="__all__"