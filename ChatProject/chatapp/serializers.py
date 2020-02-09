from rest_framework import serializers
from .models import Message , User

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Message
        fields = ['sender','receiver' ,'message']
    
    def create(self, validated_data):
        return Message.objects.create(**validated_data)    
   

# class ProfileSerializer(serializers.ModelSerializer):
#     # user = UserSerializer(source='user')
#     class Meta:
#         model = Profile
#         fields = ['phone_number']    

class UserSerializer(serializers.ModelSerializer):
    # profile = ProfileSerializer(write_only=True )
    #phone_number = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','phone_number']
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)
        # profile_data = validated_data['profile']
        # profile = None
        # if profile_data:
        #     profile = Profile.objects.get_or_create(phone_number= profile_data['phone_number'],user=)
        #     validated_data['profile'] = profile[0]
        # user = User.objects.create(**validated_data)
        # user.profile = profile[0]
        # user.save()
        # return user