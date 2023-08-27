from rest_framework import serializers


class PlayerSerializer(serializers.Serializer):

    username_player1 = serializers.CharField()
    username_player2 = serializers.CharField()


class BoardGameSerializer(serializers.Serializer):

    id_player = serializers.IntegerField()
    id_sala = serializers.IntegerField()
    option_player = serializers.IntegerField()
