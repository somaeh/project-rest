from django.db import models




class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    email = models.EmailField()
    
    
    def __str__(self):
        return self.username
    
    
    
class Todo(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='todos' )
    
    title = models.CharField(max_length=300)
    content = models.TextField()
    priority = models.IntegerField(default=1)
    is_done = models.BooleanField()
    
    
    def __str__(self):
        return self.title
        
