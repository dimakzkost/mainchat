from .models import Message
from rest_framework import serializers
import uuid


class MessageSerializer(serializers.ModelSerializer):
    text = serializers.CharField(max_length=1000)
    sender_id = serializers.UUIDField()
    receiver_id = serializers.UUIDField()
    delivered = serializers.BooleanField()
    created_at = serializers.DateTimeField()

    class Meta:
        model = Message
        fields = ['id', 'text', 'sender_id', 'receiver_id', 'delivered', 'created_at']