from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, generics, permissions
from .serializers import *
from .models import UserProfile, Task as Task_Model, Attendance
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from datetime import date

# Create your views here.

# API Overview
@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Sign In': '/login/',
        'Register': '/register/',
        'User Lists': '/user-list/',

        'Profile Operations': '/profile/<pk>/',
        'Profile Lists': '/profile-list/',

        'Create Task': '/create-task/',
        'Task Operation': '/task/<str:pk>',
        'Assigned Task List':'/assigned-task/',
        'Assigned Task Detail': '/assigned-task/<str:pk>/',
        'Task Lists': '/task-list/',

        'Create Attendance': '/create-attendance/',
        'Attendance Operation': '/attendance/<str:pk>/',
        'Mark As Present': '/mark_as_present/',
        'Attendance List': '/attendance-list/',
    }
    return Response(api_urls)


# User Management
# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        auth_token = Token.objects.get(user=user)
        data_responce = {
            'data': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': auth_token.key
        }
        return Response(data_responce)


class User_List(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        if user_profile.role == 'Supervisor':
            User_List = User.objects.all()
            serializer = UserSerializer(User_List, many=True)
            return Response(serializer.data)
        else:
            return Response({'Error': 'You are not allow to see, Only supervisor can see this.'})


# User Profile
class User_Profile_List(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        if user_profile.role == 'Supervisor':
            profile_list = UserProfile.objects.all()
            serializer = UserProfileSerializerAll(profile_list, many=True)
            return Response(serializer.data)
        else:
            return Response({'Error': 'You are not allow to see, Only supervisor can see this.'})



class User_Profile(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileSerializer
    def get(self, request, pk):
        user_profile = UserProfile.objects.get(user=request.user)
        profile = UserProfile.objects.get(id=pk)
        if user_profile.role == 'Supervisor':
            serializer = UserProfileSerializerAll(profile, many=False)
            return Response(serializer.data)
        elif request.user == profile.user:
            serializer = UserProfileSerializerAll(profile, many=False)
            return Response(serializer.data)
        else:
            return Response({'Error': 'You are note authorized to see!'})

    def post(self, request, pk):
        user_profile = UserProfile.objects.get(user=request.user)
        if user_profile.role == 'Supervisor':
            profile = UserProfile.objects.get(id=pk)
            serializer = UserProfileSerializerSupervisor(instance=profile, data=request.data)
        else:
            profile = UserProfile.objects.get(id=pk)
            serializer = UserProfileSerializer(instance=profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)
    def delete(self, request, pk):
        user_profile = UserProfile.objects.get(user=request.user)
        if user_profile.role == 'Supervisor':
            profile = UserProfile.objects.get(id=pk)
            profile.delete()
            return Response({'Success':'Successfully Deleted!'})
        else:
            return Response({'Error': 'You are note authorized to deleted profile!'})

# Task
class Task_List(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        if user_profile.role == 'Supervisor':
            task_list = Task_Model.objects.all()
            serializer = TaskSerializer(task_list, many=True)
            return Response(serializer.data)
        else:
            return Response({'Error': 'You are note authorized to see!'})

class Create_Task(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer
    def post(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        if user_profile.role == 'Supervisor':
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response({'Error': 'You are note authorized to see!'})

class Assigned_Task_Operation_List(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileSerializer
    def get(self, request):
        profile = UserProfile.objects.get(user=request.user)
        tasks = Task_Model.objects.filter(assigned=profile)
        if len(tasks) >= 1:
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data)
        else:
            return Response({'Error': 'You do not have any task.'})

class Assigned_Task_Operation_Detail(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileSerializer
    def get(self, request, pk):
        task = Task_Model.objects.get(id = pk)
        profile = UserProfile.objects.get(user=request.user)
        if task.assigned == profile:
            serializer = TaskSerializer(task, many=False)
            return Response(serializer.data)
        else:
            return Response({'Error': 'You are note authorized to see!'})
    def post(self, request, pk):
        task = Task_Model.objects.get(id=pk)
        profile = UserProfile.objects.get(user=request.user)
        if task.assigned == profile:
            serializer = TaskSerializerIntern(instance=task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response({'Error': 'You are note authorized to see!'})

class Task_Operation(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer
    def get(self, request, pk):
        user_profile = UserProfile.objects.get(user=request.user)
        task = Task_Model.objects.get(id=pk)
        if user_profile.role == 'Supervisor':
            serializer = TaskSerializer(task, many=False)
            return Response(serializer.data)
        elif request.user == task.assigned.user:
            serializer = TaskSerializer(task, many=False)
            return Response(serializer.data)
        else:
            return Response({'Error': 'You are note authorized to see!'})

    def post(self, request, pk):
        user_profile = UserProfile.objects.get(user=request.user)
        if user_profile.role == 'Supervisor':
            task = Task_Model.objects.get(id=pk)
            serializer = TaskSerializerSupervisor(instance=task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response({'Error': 'You are note authorized to see!'})

    def delete(self, request, pk):
        user_profile = UserProfile.objects.get(user=request.user)
        if user_profile.role == 'Supervisor':
            task = Task_Model.objects.get(id=pk)
            task.delete()
            return Response({'Success':'Successfully Deleted!'})
        else:
            return Response({'Error': 'You are note authorized to deleted profile!'})


# Attendance
class Attendance_List(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        if user_profile.role == 'Supervisor':
            print("first")
            attendance_list = Attendance.objects.all()
            serializer = AttendanceSerializer(attendance_list, many=True)
            return Response(serializer.data)
        elif user_profile.role == 'Intern':
            print('second')
            attendance_list = Attendance.objects.filter(username=user_profile)
            serializer = AttendanceSerializer(attendance_list, many=True)
            return Response(serializer.data)
        else:
            return Response({'Error': 'You are note authorized to see!'})

class Make_As_Present(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        user_profile = UserProfile.objects.get(user=request.user)
        attendance_status = Attendance.objects.filter(username=user_profile, date=date.today())
        if len(attendance_status) < 1:
            attend = Attendance.objects.create(username=user_profile, date=date.today(), attendence_status=True)
            attend.save()
            serializer = AttendanceSerializer(attend, many=False)
            return Response(serializer.data)
        else:
            data = {
                'date': date.today(),
                'attendance_status': True
            }
            return Response({'data': data, 'Done':'Already Done!'})


class Attendance_Operations(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AttendanceSerializer
    def get(self, request, pk):
        user_profile = UserProfile.objects.get(user=request.user)
        attendance = Attendance.objects.get(id=pk)
        if user_profile.role == 'Supervisor':
            serializer = AttendanceSerializer(attendance, many=False)
            return Response(serializer.data)
        elif user_profile == attendance.username:
            serializer = AttendanceSerializer(attendance, many=False)
            return Response(serializer.data)
        else:
            return Response({'Error': 'You are note authorized to see!'})

    def post(self, request, pk):
        user_profile = UserProfile.objects.get(user=request.user)
        if user_profile.role == 'Supervisor':
            attendance = Attendance.objects.get(id=pk)
            serializer = MakeAttendanceSerializer(instance=attendance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response({'Error': 'You are note authorized to see!'})

    def delete(self, request, pk):
        user_profile = UserProfile.objects.get(user=request.user)
        if user_profile.role == 'Supervisor':
            attendance = Attendance.objects.get(id=pk)
            attendance.delete()
            return Response({'Success':'Successfully Deleted!'})
        else:
            return Response({'Error': 'You are note authorized to deleted profile!'})
