from rest_framework import serializers
from .models import Message , User

class MessageSerializer(serializers.ModelSerializer):
    reg_google = serializers.StringRelatedField(source='receiver.reg_google',read_only=True)
    class Meta:
        model  = Message
        fields = ['sender','receiver' ,'message','reg_google','id']
    
    def create(self, validated_data):
        return Message.objects.create(**validated_data)    
     

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    class Meta:
        model = User
        fields = ['username','phone_number']
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)

class ProfileSerializer(serializers.Serializer):
    image_url = serializers.SerializerMethodField('get_image_url') #serializers.ImageField(required=True,use_url=True)

    def get_image_url(self, obj):
        print("Hello world")
        print(obj)
        return obj