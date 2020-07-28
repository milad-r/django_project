from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('users/', views.users , name="user_list"),
    path('messages/', views.Messages, name="messages"),
    path('send-message/' , views.message_view ),
    path('seen/' , views.Seen , name= 'seen' ),
    path('register/', views.Register , name='register'),
    path('login/', views.Login , name='login'),
    path('setprofile', views.SetProfile , name="setprofile"),
    path('set_reg-google' , views.Set_Reg ),
    path('set_read', views.Set_Read  ),
    path('profile', views.Profile  ),

]

