from django.urls import path
from.import views


urlpatterns=[
    path('todo', views.all_todo, name='all_todo'),
    path('user', views.all_user, name='all_user'),
    path('<int:todo_id>', views.todo_details_view),
    path('cbv/', views.TodosListApiview.as_view()),
    path('cbv/<int:todo_id>', views.TodosDetailApiview.as_view()),
    path('mixins/', views.TodosListMixinsApiview.as_view()),
    path('mixins/<int:pk>', views.TodosDetailMixinsApiview.as_view()),
  
    
]