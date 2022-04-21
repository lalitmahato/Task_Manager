from django.urls import path, include
from . import views
# from knox import views as knox_views
from rest_framework.authtoken import views as auth_token_view


urlpatterns = [
    path('',views.api_overview, name='api_overview'),
    path('register/', views.RegisterAPI.as_view(), name='register_user'),
    path('login/', auth_token_view.obtain_auth_token, name='user_login'),
    # path('logout/',knox_views.LogoutView.as_view(),name='user_logout'),
    path('user-list/', views.User_List.as_view(), name='user_list'),

    path('profile-list/', views.User_Profile_List.as_view(), name='profile_list'),
    path('profile/<str:pk>', views.User_Profile.as_view(), name='profile_detail'),


    path('task-list/', views.Task_List.as_view(), name='task_list'),
    path('create-task/', views.Create_Task.as_view(), name='create_list'),
    path('assigned-task/',views.Assigned_Task_Operation_List.as_view(), name='assign_task'),
    path('assigned-task/<str:pk>',views.Assigned_Task_Operation_Detail.as_view(), name='assign_task'),
    path('task/<str:pk>', views.Task_Operation.as_view(), name='task_detail'),


    path('attendance-list/', views.Attendance_List.as_view(), name='attendance_list'),
    path('mark_as_present/', views.Make_As_Present.as_view(), name='mark_as_present'),
    path('attendance/<str:pk>', views.Attendance_Operations.as_view(), name='attendance_operation')
]