from django.urls import path

from ...matches.api import views

app_name = "matches_api"

urlpatterns = [
    path("api/v1/board_game/create/", views.BoardGameCreateAPIView.as_view(), name="board_game_create",),
    path("api/v1/board_game/list/<int:id_board>/", views.BoardGameGetAPIView.as_view(), name="board_game_list",),
    path("api/v1/board_game/turn_create/", views.TurnBoardGameCreateAPIView.as_view(), name="board_game_turn_create",)

    ]