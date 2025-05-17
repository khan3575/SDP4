# connect4_backend/api/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Match

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

class MatchSerializer(serializers.ModelSerializer):
    player1_username = serializers.ReadOnlyField(source='player1.username')
    
    class Meta:
        model = Match
        fields = ['id', 'date', 'player1', 'player1_username', 'player2', 'winner']
        extra_kwargs = {'player1': {'write_only': True}}