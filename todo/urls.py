from . import views
from django.urls import path 

urlpatterns = [
    path('',views.home,name='home_todo'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),  
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
