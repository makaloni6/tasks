from django.urls import path, include
from .views import TaskView
from . import views
from rest_framework import routers
from django.contrib import admin
from todo import views
from django.views.generic import TemplateView


router = routers.DefaultRouter()
router.register(r'todos', views.TaskView, 'todo')


urlpatterns = [
    # path('', views.index, name='index'),
    path('tasks_list/', TaskView.task, name='tasks_list'),
    path('tasks/', TaskView.task_post, name='tasks'),
    path('admin/', admin.site.urls),
    path('api/', TemplateView.as_view(template_name='todo/index.html')),
    # path('api/', include('todo.urls')),
    # path('form', TodoView.form, name='form')
    # path('<int:user_id>/', views.task, name='task')
]