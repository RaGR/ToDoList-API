from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Task
from .serializer import TaskSerializer,UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User



# Create your views here.

#AUTH classes
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class UserView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
#AUTH classes


class TaskViewSet(viewsets.ModelViewSet, generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)



class TaskList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.filter(user=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

class TaskDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            usr_tasks = Task.objects.all().filter(user=self.request.user)
            print(usr_tasks)
            task = usr_tasks.objects.get(pk=pk, user=self.request.user)
            return task
        except Task.DoesNotExist:
            return None

    def get(self, request, pk):
        usr_tasks = Task.objects.all().filter(user=self.request.user)
        print(usr_tasks)
        task = self.get_object(pk)
        if not task:
            return Response({'error': 'Task not found'}, status=404)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        if not task:
            return Response({'error': 'Task not found'}, status=404)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        task = self.get_object(pk)
        if not task:
            return Response({'error': 'Task not found'}, status=404)
        task.delete()
        return Response(status=204)