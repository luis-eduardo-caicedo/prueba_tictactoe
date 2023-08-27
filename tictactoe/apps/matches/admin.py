from django.contrib import admin
from .models import Matches, BoardGame

@admin.register(Matches)
class MatchesAdmin(admin.ModelAdmin):
    list_display = ['id', 'winner', 'player1', 'player2']


@admin.register(BoardGame)
class BoardGameAdmin(admin.ModelAdmin):
    list_display = ['id', 'player_turn', 'player1', 'player2']
    
