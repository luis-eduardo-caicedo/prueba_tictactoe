from django.db import models
from ..player.models import Player

class Matches(models.Model):
    player1 = models.ForeignKey(
        Player,
        on_delete=models.PROTECT,
        verbose_name="Jugador 1",
        related_name='matches_player1'
    )
    player2 = models.ForeignKey(
        Player,
        on_delete=models.PROTECT,
        verbose_name="Jugador 2",
        related_name='matches_player2'
    )
    winner = models.ForeignKey(
        Player,
        on_delete=models.PROTECT,
        verbose_name="Ganador",
        related_name='matches_winner'
    )
    date_created = models.DateTimeField("Fecha Creación", auto_now_add=True)
    

    def __str__(self):
        return self.winner
    
    class Meta:
        verbose_name = "Encuentro"
        verbose_name_plural = "Encuentros"


class BoardGame(models.Model):

    player1 = models.ForeignKey(
        Player,
        on_delete=models.PROTECT,
        verbose_name="Jugador 1",
        related_name='boardgame_player1'
    )
    player2 = models.ForeignKey(
        Player,
        on_delete=models.PROTECT,
        verbose_name="Jugador 2",
        related_name='boardgame_player2'

    )

    player_turn = models.ForeignKey(
        Player,
        on_delete=models.PROTECT,
        verbose_name="Turno del jugador",
        related_name='boardgame_player_turn',
        null=True, 
        blank=True
    )

    options_player1 = models.TextField(max_length=254, null=True, blank=True)
    options_player2 = models.TextField(max_length=254, null=True, blank=True)
    options_totals = models.TextField(max_length=254, null=True, blank=True)
    
    def __str__(self):
        return self.player1.username
    
    class Meta:
        verbose_name = "Tablero"
