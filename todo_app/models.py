from django.db import models



class Todo(models.Model):
        title = models.CharField(max_length=300)
        content = models.TextField()
        priority = models.IntegerField(default=1)
        is_done = models.BooleanField()
        
        
        def __str__(self):
            return self.title
