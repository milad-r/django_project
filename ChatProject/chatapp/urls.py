from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('users/', views.users , name="user_list"),
    path('messages/<str:sender>/<str:receiver>/', views.Messages, name="messages"),
    path('send-message/' , views.message_view ),
    path('register/', views.Register , name='register'),
    path('login/', views.Login , name='login'),


]

