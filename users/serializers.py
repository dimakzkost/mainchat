from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)


    class Meta:
        model = User
        fields = ['id', 'username']