from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('meeting/', views.videocall, name='meeting'),
    path('join_room/', views.join_room, name='join_room'),
    path('random_call/', views.random_call, name='random_call'),
]
