from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index , name='index'),
    path('users/<int:user_id>/', views.users , name="user_list"),
    path('messages/', views.messages, name="all_messages"),
    path('messages/<int:sender>/<int:receiver>/', views.messages, name="messages"),
]
