from django.urls import path
from . import views
from django.contrib.auth import views as log_views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('home/', views.HomeView.as_view(template_name='TodoList/home.html'), name='home'),
    path('logout/', log_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('todolist/<str:username>/', views.TaskListView.as_view(), name='todolist-main'),
    path('todolist/<str:username>/<int:task_id>/completed', views.mark_complete, name='todolist-complete'),
    path('todolist/create-task', views.TaskCreateView.as_view(), name='create-task')
]

