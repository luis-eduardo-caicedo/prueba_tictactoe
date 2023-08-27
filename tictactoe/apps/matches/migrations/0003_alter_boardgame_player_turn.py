# Generated by Django 4.2.4 on 2023-08-25 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
        ('matches', '0002_alter_boardgame_options_player1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardgame',
            name='player_turn',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='boardgame_player_turn', to='player.player', verbose_name='Turno del jugador'),
        ),
    ]