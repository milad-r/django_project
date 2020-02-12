from django.shortcuts import render , redirect
from django.http import HttpResponse , JsonResponse 
from rest_framework.parsers import JSONParser , MultiPartParser
from .serializers import UserSerializer , MessageSerializer 
from .models import Message , User
from itertools import chain
import operator
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.exceptions import APIException
from kavenegar import *
from random import randint

def index(request):
    user = request.user
    if user.is_authenticated:
        return redirect('chats')
    else:
        return redirect('login')

@api_view(['POST'])
@parser_classes([JSONParser])
def Messages(request):
    data = request.data
    sender = data['sender']
    receiver= data['receiver']
    messages1 = Message.objects.filter(sender = sender , receiver = receiver)
    messages2 = Message.objects.filter(sender =receiver , receiver=sender)
    messages  = list(chain(messages1 , messages2))
    messages = sorted(messages , key=operator.attrgetter('timestamp'))
    serializer = MessageSerializer(messages , many=True , context={'request': request})
    return JsonResponse(serializer.data, json_dumps_params={'ensure_ascii': False}, safe=False)



@api_view(['POST'])
@parser_classes([JSONParser])
def message_view(request):
    """
    A view that can accept message and create an message object in server
    """
    data = request.data
    serializer = MessageSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)    
    return JsonResponse(serializer.errors, status=400)


@api_view(['POST'])
@parser_classes([JSONParser])
def Register(request):
    data = request.data
    token = randint(100000, 999999)
    try:
        api = KavenegarAPI('4872465463763051536E44756259536567304F4449777257384A565455356567456A6C30476B4B6D6D304D3D')
        params = {
            'receptor': data['phone_number'] ,
            'token' : token ,
            'template': 'verify',
        }   
        response = api.verify_lookup(params)
        print(response)

        return JsonResponse({'token':token ,'number':response['receptor']})
    except APIException as e: 
            return JsonResponse(str(e))
    except Exception as e: 
            return JsonResponse(str(e))

@api_view(['POST'])
@parser_classes([JSONParser])
def Login(request):
    data = request.data  
    try :
        p = data['phone_number']
        user = User.objects.get(phone_number=p)
        srializer = UserSerializer(user)
        return JsonResponse(srializer.data, status=201)
    except User.DoesNotExist :
        serializer = UserSerializer(data=data)
        if serializer.is_valid():    
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['POST'])
@parser_classes([JSONParser , MultiPartParser])
def SetProfile(request):
    data = request.data
    #return HttpResponse(request.data['username'])
    #user = data.get('username')
    user = request.POST['username']
    image = request.FILES['image']
    #return HttpResponse(user)
    user = User.objects.get(username=user)
    user.profile_image = image
    user.save()
    return render(request,'messageform.html',{'image':image})
    return JsonResponse({'success':True})

@api_view(['POST'])
@parser_classes([JSONParser])
def users(request):
    user = request.data['username']
    users = User.objects.exclude(username=user)
    serializer = UserSerializer(users, many=True ,)
    return JsonResponse(serializer.data , safe=False)
