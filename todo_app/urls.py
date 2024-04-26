from django.urls import path, include
from.import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.TodoViewApiview)
urlpatterns=[
    path('todo', views.all_todo, name='all_todo'),
    path('user', views.UsersGenericApiview.as_view()),
    path('<int:todo_id>', views.todo_details_view),
    path('cbv/', views.TodosListApiview.as_view()),
    path('cbv/<int:todo_id>', views.TodosDetailApiview.as_view()),
    path('mixins/', views.TodosListMixinsApiview.as_view()),
    path('mixins/<int:pk>', views.TodosDetailMixinsApiview.as_view()),
    path('generics/', views.TodoGenericApiview.as_view()),
    path('generics/<int:pk>', views.TodoGenericDtailApiview.as_view()),
    path('viewsets/', include(router.urls))

  
    
]