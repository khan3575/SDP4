# connect4_backend/api/views.py

from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import Match
from .serializers import UserSerializer, MatchSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class MatchListCreateView(generics.ListCreateAPIView):
    serializer_class = MatchSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Match.objects.filter(player1=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(player1=self.request.user)# connect4_backend/api/views.py

from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import Match
from .serializers import UserSerializer, MatchSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class MatchListCreateView(generics.ListCreateAPIView):
    serializer_class = MatchSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Match.objects.filter(player1=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(player1=self.request.user)