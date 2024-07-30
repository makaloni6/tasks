from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from .serializers import TaskSerializer
from rest_framework import viewsets
from django.forms.models import model_to_dict

from .forms import  TodoForm
from .models import Task
import json

from django.views.generic import TemplateView

class TaskView(viewsets.ModelViewSet):
    # Create your views here.
    page_max = 10

    @login_required(login_url='/admin/login/')
    def index(request):
        print('index')
        queryset = Task.objects.all()

        return render(request, 'index.html', queryset)

    #taskの取得
    @login_required(login_url='/admin/login/')
    def task(request, page=1):
        print('task')
        serializer_class = TaskSerializer
        tasks = Task.objects.all()
        serialized_data = serialize('json', tasks)
        return HttpResponse(serialized_data, content_type='application/json')

    #taskのポスト処理
    @login_required(login_url='/admin/login/')
    def task_post(request):
        if request.method == 'POST':
            byte_data = request.body.decode('utf-8')
            json_body = json.loads(byte_data)

            task = Task()
            task.title = json_body['title']
            task.description = json_body['description']
            task.due_date = json_body['due_date']
            task.actual_time = json_body['actual_time']
            task.is_completed = json_body['is_completed']

            task.save()
            return HttpResponse('ok')
        
        else:
            return HttpResponse('ng')
        
