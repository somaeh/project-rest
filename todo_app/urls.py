from django.urls import path
from.import views


urlpatterns=[
    path('', views.all_todo, name='all_todo'),
    path('user', views.all_user, name='all_user'),
]