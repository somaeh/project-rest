from django.contrib import admin
from .models import Todo

# @admin.register(models.Todo)
# class TodoAdmin(admin.ModelAdmin):
#     pass

# # Register your models here.
admin.site.register(Todo)
