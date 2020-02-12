from rest_framework import serializers
from .models import Message , User

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Message
        fields = ['sender','receiver' ,'message']
    
    def create(self, validated_data):
        return Message.objects.create(**validated_data)    
     

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    class Meta:
        model = User
        fields = ['username','phone_number']
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)