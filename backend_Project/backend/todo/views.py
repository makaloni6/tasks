from .serializers import TaskSerializer, TaskLogSerializer
from rest_framework import viewsets
from .models import Task, TaskLog

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
# from rest_framework_simplejwt.tokens import RefreshToken

class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskLogView(viewsets.ModelViewSet):
    queryset = TaskLog.objects.all()
    serializer_class = TaskLogSerializer


# @api_view(['POST'])
# def login_view(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         # ユーザーが存在する場合の処理
#         return Response({'message': 'Login successful'})
#     else:
#         # ユーザーが存在しない場合の処理
#         return Response({'message': 'Invalid credentials'}, status=400)
    
class LoginView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            # refresh = RefreshToken.for_user(user)
            return Response({
                {'message': 'Login successful'}
            })
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)