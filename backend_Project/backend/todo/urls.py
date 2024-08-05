from django.urls import path, include
from .views import TaskView, TaskLogView, LoginView
from rest_framework import routers
from django.contrib import admin
from todo import views
from django.views.generic import TemplateView


router = routers.DefaultRouter()
router.register(r'tasks', TaskView, 'todo')
router.register(r'tasklogs', TaskLogView, 'todolog')


urlpatterns = [
    # path('', views.index, name='index'),
    # path('tasks_list/', TaskView.task, name='tasks_list'),
    # path('tasks/', TaskView.task_post, name='tasks'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),

    # path('form', TodoView.form, name='form')
    # path('<int:user_id>/', views.task, name='task')
]