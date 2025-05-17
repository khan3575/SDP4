# connect4_backend/api/models.py

from django.db import models
from django.contrib.auth.models import User

class Match(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    player1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='matches_as_player1')
    player2 = models.CharField(max_length=100, default="Local Guest")
    winner = models.CharField(max_length=100)  # "player1", "player2", or "draw"
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d %H:%M')} - {self.player1.username} vs {self.player2}"