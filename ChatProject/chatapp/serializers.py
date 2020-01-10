from rest_framework import serializers
from .models import Message , Profile

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Message
        fields = ['sender','receiver' ,'message']