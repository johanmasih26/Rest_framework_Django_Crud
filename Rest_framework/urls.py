from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path('tasklist',views.taskList,name="tasklist"),
    path('taskdetail/<int:pk>/',views.taskDetail,name="taskdetail"),
    path('taskUpdate/<int:pk>/',views.taskUpdate,name="taskupdate"),
    path('taskDelete/<int:pk>/',views.taskDelete,name="taskdelete"),
    path('taskcreate/',views.taskcreate,name="taskcreate"),
]



