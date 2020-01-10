from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User


def index(request):
    
    if request.user.is_authenticated:
        return render(request, 'chats.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            return HttpResponse('{"error": "User does not exist"}')
    else:
        return redirect('login')

def messages(request , sender=None ,receiver=None):
    return HttpResponse('This view return all messages or messages between two user')


def users(request,user_id):
    users = User.objects.all()

    context = {
        'users':users,
    }
    return render(request ,'users.html' ,context)