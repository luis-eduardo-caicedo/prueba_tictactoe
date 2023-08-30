import json

from rest_framework.response import Response
from rest_framework import generics
from ...matches import models as models_matches
from ...player import models as models_players
from ...matches.api import serializers as serializers_matches


tablero2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

options_win = [
    [ 1, 2, 3], #Vertical fila 1
    [ 4, 5, 6], #Vertical fila 2
    [ 7, 8, 9], #Vertical fila 3
    [ 1, 4, 7], #Horizontal columna 1
    [ 2, 5, 8], #Horizontal columna 2
    [ 3, 6, 9], #Horizontal columna 3
    [ 1, 5, 9], #Diagonal Izquierda a derecha
    [ 7, 5, 3]  #Diagonal Derecha a izquierda
]

#**************FUNCIONES*************************

def imprimir_tablero(tablero):
    output = ""
    for fila in tablero:
        output += "".join(map(str, fila)) + "\n"

    board_eraser = f'{output[0]}|{output[1]}|{output[2]}'
    board_eraser2 = f'{output[4]}|{output[5]}|{output[6]}'
    board_eraser3 = f'{output[8]}|{output[9]}|{output[10]}'

    board_total = [board_eraser , board_eraser2 , board_eraser3]
    return board_total


def match_tablero(num, tablero, indicador):
    if num == 1:
        tablero[0][0] = indicador
    elif num == 2:
        tablero[0][1] = indicador
    elif num == 3:
        tablero[0][2] = indicador
    elif num == 4:
        tablero[1][0] = indicador
    elif num == 5:
        tablero[1][1] = indicador
    elif num == 6:
        tablero[1][2] = indicador
    elif num == 7:
        tablero[2][0] = indicador
    elif num == 8:
        tablero[2][1] = indicador
    elif num == 9:
        tablero[2][2] = indicador


def dibujar_tablero (opt_player, indicador, tabla):
    
    if opt_player:
        for num in opt_player:
            match_tablero(num, tabla, indicador)

    return tabla


def verificar_ganador(options_win, options_player):
    for reg in options_win:
        if set(reg).issubset(options_player):
            player_win = True
            return player_win


class BoardGameCreateAPIView(generics.CreateAPIView):
    """
    Esta View se encarga de crear un tablero para los jugadores 2 que se ingresaran
    """

    serializer_class = serializers_matches.PlayerSerializer

    def post(self, request, *args, **kwargs):

        player1 = request.data["username_player1"]
        player2 = request.data["username_player2"]

        user_player1 = models_players.Player.objects.filter(username=player1).last()
        data_user1 = {
            "username": player1
        }

        # Se valida si el nombre de usuario que agregaron para el jugador existe
        # Si no existe se crea y se guarda el ID

        if not user_player1:
            user_player1 = models_players.Player.objects.create(**data_user1)
            user_player1.save()

        #*********************************************
        user_player2 = models_players.Player.objects.filter(username=player2).last()
        data_user2 = {
            "username": player2
        }

        # Se valida si el nombre de usuario que agregaron para el jugador existe
        # Si no existe se crea y se guarda el ID

        if not user_player2:
            user_player2 = models_players.Player.objects.create(**data_user2)
            user_player2.save()

        data_sala = {
            "player1": user_player1,
            "player2": user_player2
        }

        # Se crea un nuevo tablero con los jugadores que van a jugar
        # Hay una respuesta en la cual aparecera el tablero, los ID's
        # De los jugadores y el ID de la sala/tablero

        sala = models_matches.BoardGame.objects.create(**data_sala)
        sala.save()

        data_seri = {
            "board1": imprimir_tablero(tablero2)[0],
            "board2": imprimir_tablero(tablero2)[1],
            "board3": imprimir_tablero(tablero2)[2],
            "player1": f'{user_player1.username}, vas a jugar con el id #{user_player1.id}',
            "player2": f'{user_player2.username}, vas a jugar con el id #{user_player2.id}',
            "sala": f'El numero del tablero es: {sala.id}'
        }
    
        return Response(data=data_seri)


class BoardGameGetAPIView(generics.ListAPIView):
    """
    Esta View se encarga de traer el tablero con los movimientos que han hecho los jugadores
    """
     
    def get(self, *args, **kwargs):

        copy_tabla = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        id_board = self.kwargs["id_board"]

        query_board = models_matches.BoardGame.objects.filter(id=id_board).last()

        # Se valida que el ID de la partida que fue recibido existe o no

        if not query_board:
            return Response("Esta partida no existe...")

        #**********************************************
        # En la siguiente condicion se valida sí el jugador 1 ha tenido movimientos
        # En el caso de que sí tenga, se cargan los datos y se convierte en una lista
        # Se dibuja el tablero con los movimientos que tiene el jugador y luego se verifica
        # Si con los movimientos que tiene es ganador

        if query_board.options_player1:
            options_player1 = json.loads(query_board.options_player1)
            ejemplo1 = dibujar_tablero(options_player1, "X", copy_tabla)
            verify_win = verificar_ganador(options_win, options_player1)
            data_win = {
                "board1": imprimir_tablero(ejemplo1)[0],
                "board2": imprimir_tablero(ejemplo1)[1],
                "board3": imprimir_tablero(ejemplo1)[2],
                "******": "******",
                f'player1 (X)': query_board.player1.username,
                "player2 (O)": query_board.player2.username,
                "Winner": query_board.player1.username
            }
            if verify_win:
                return Response(data=data_win)
        else:
            options_player1 = []
            ejemplo1 = copy_tabla

        #**********************************************
        # En la siguiente condicion se valida sí el jugador 2 ha tenido movimientos
        # En el caso de que sí tenga, se cargan los datos y se convierte en una lista
        # Se dibuja el tablero con los movimientos que tiene el jugador y luego se verifica
        # Si con los movimientos que tiene es ganador

        if query_board.options_player2:
            options_player2 = json.loads(query_board.options_player2)
            ejemplo2 = dibujar_tablero(options_player2, "O", ejemplo1)
            verify_win = verificar_ganador(options_win, options_player2)
            data_win = {
                "board1": imprimir_tablero(ejemplo2)[0],
                "board2": imprimir_tablero(ejemplo2)[1],
                "board3": imprimir_tablero(ejemplo2)[2],
                "******": "******",
                "player1 (X)": query_board.player1.username,
                "player2 (O)": query_board.player2.username,
                "Winner": query_board.player2.username
            }
            if verify_win:
                return Response(data=data_win)
        else:
            options_player2 = []
            ejemplo2 = copy_tabla

        #**********************************************
        # Se valida si hay datos en el campo de movimientos totales
        # En el caso de que hayan se cargan y se convierten en una lista
        # Luego se valida si entre los dos jugadores completaron el numero
        # Maximo de movimientos para acabar en empate

        if query_board.options_totals:
            options_totals = json.loads(query_board.options_totals)
            if len(options_totals) > 8:
                data_draw = {
                "******": "******",
                "player1 (X)": query_board.player1.username,
                "player2 (O)": query_board.player2.username,
                "message": "La partida ha terminado en empate ..."
            }
                return Response(data=data_draw)    
        else:
            ejemplo2 = copy_tabla
            options_totals = []

        #**********************************************
        # En el caso de que no hayan movimientos del jugador 1 ni del jugador 2
        # Se cargara la tabla original para mostrar en la respuesta

        if not query_board.options_player1 or not query_board.options_player2:
            ejemplo2 = copy_tabla

        data = {
            "board1": imprimir_tablero(ejemplo2)[0],
            "board2": imprimir_tablero(ejemplo2)[1],
            "board3": imprimir_tablero(ejemplo2)[2],
            "******": "******",
            f'player1 (X) id: {query_board.player1.id}': query_board.player1.username,
            f'player2 (O) id: {query_board.player2.id}': query_board.player2.username,
        }

        return Response(data=data)


class TurnBoardGameCreateAPIView(generics.CreateAPIView):
    """
    Esta View se encarga de crear un el movimiento que hará un jugador con su id para identificarlo
    y el numero del tablero y ademas la posicion en la que quiere jugar
    """ 

    serializer_class = serializers_matches.BoardGameSerializer

    def post(self, request, *args, **kwargs):

        id_player = request.data["id_player"]
        id_board = request.data["id_sala"]
        option_player = request.data["option_player"]

        #Se establece una copia del tabler para la logica que se establece más adelante
        copy_tabla = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        ejemplo2 = copy_tabla
        original_table = tablero2

        #Estas son validaciones para que los datos no vengan vacios
        if not id_board :
            return Response("Tiene que agregar un id de la sala")
        if not id_player:
            return Response("Tiene que agregar un id del Jugador")
        if not option_player:
            return Response("Tiene que agregar una posicion de la tabla")
        if not 0 < int(option_player) < 10:
            return Response("Opcion valida")

        query_board = models_matches.BoardGame.objects.filter(id=id_board).last()
        current_player = models_players.Player.objects.filter(id=id_player).last()
        

        if not current_player:
            return Response("Este jugador no existe...")
        
        if not query_board:
            return Response("Esta partida no existe...")
        
        if query_board.player1 != current_player and query_board.player2 != current_player:
            return Response("Usted no esta en esta partida")

        #**********************************************
        # Se valida que venga datos en el campo de optiones totales
        # Luego de esto se valida si ya los jugadores utilizaron sus
        # Movimientos y apartir de este resultado se daria un empate
        # O en el caso de que no los hayan utilizado todo, verificar
        # Que no se repite el movimiento en la misma posicion
        if query_board.options_totals:
            options_totals = json.loads(query_board.options_totals)
            if len(options_totals) > 8:
                return Response("'response': La partida se ha terminado")
            if int(option_player) in options_totals:
                data2 = {
                        "board1": imprimir_tablero(original_table)[0],
                        "board2": imprimir_tablero(original_table)[1],
                        "board3": imprimir_tablero(original_table)[2],
                        "******": "******",
                        "message": "Posicion invalida, debe elejir otra posicion del tablero...",
                    }

                return Response(data=data2)
        else:
            ejemplo2 = copy_tabla

        #*********************************************************
        # se valida si el jugador 1 ha realizado movimientos, en el caso de
        # que los haya hecho, se agregaran a la lista los siguientes movimientos
        # y luego de esto se agrega tambien el movimiento en el campo de 
        # opciones totales
        # Luego se dibuja el tablero y se verifica si con el movimiento que realizo
        # gano la partida o sigue jugando
        if query_board.options_player1:
            
            options_player1 = json.loads(query_board.options_player1)
            if query_board.player1 == current_player:
                options_player1.append(int(option_player))
                query_board.options_player1 = json.dumps(options_player1)

                options_totals_data = json.loads(query_board.options_totals)
                options_totals_data.append(int(option_player))
                query_board.options_totals = json.dumps(options_totals_data)
                query_board.save()

            ejemplo1 = dibujar_tablero(options_player1, "X", copy_tabla)
            verify_win = verificar_ganador(options_win, options_player1)
            if verify_win:
                return Response(f'Ganador Jugador #1 {query_board.player1.username}')
            
        # Si el jugador no ha realizado ningun movimiento se crea una lista nueva con el
        # movimiento que agrego y se agrega al campo tablero
        else:
            if query_board.player1.id == current_player.id:

                options_player1 = []
                options_player1.append(int(option_player))
                query_board.options_player1 = json.dumps(options_player1)
                
                if query_board.options_totals:
                    options_totals = json.loads(query_board.options_totals)
                    options_totals.append(int(option_player))
                    query_board.options_totals = json.dumps(options_totals)
                    query_board.save()

 
                else:
                    options_totals = []
                    options_totals.append(int(option_player))
                    query_board.options_totals = json.dumps(options_totals)
                    query_board.save()

            ejemplo1 = copy_tabla

        #*********************************************************
        #*********************************************************
        # se valida si el jugador 2 ha realizado movimientos, en el caso de
        # que los haya hecho, se agregaran a la lista los siguientes movimientos
        # y luego de esto se agrega tambien el movimiento en el campo de 
        # opciones totales
        # Luego se dibuja el tablero y se verifica si con el movimiento que realizo
        # gano la partida o sigue jugando

        if query_board.options_player2:

            options_player2 = json.loads(query_board.options_player2)
            if query_board.player2 == current_player:

                options_player2.append(int(option_player))
                query_board.options_player2 = json.dumps(options_player2)

                options_totals_data = json.loads(query_board.options_totals)
                options_totals_data.append(int(option_player))
                query_board.options_totals = json.dumps(options_totals_data)
                query_board.save()

            ejemplo2 = dibujar_tablero(options_player2, "O", ejemplo1)
            verify_win = verificar_ganador(options_win, options_player2)
            if verify_win:
                return Response(f'Ganador Jugador #2 {query_board.player2.username}')
            
        # Si el jugador no ha realizado ningun movimiento se crea una lista nueva con el
        # movimiento que agrego y se agrega al campo tablero    

        else:

            if query_board.player2.id == current_player.id:

                options_player2 = []
                options_player2.append(int(option_player))
                query_board.options_player2 = json.dumps(options_player2)
                
                if query_board.options_totals == "":
                    options_totals = []
                    options_totals.append(int(option_player))
                    query_board.options_totals = json.dumps(options_totals)
                    query_board.save()
                else:
                    options_totals = json.loads(query_board.options_totals)
                    options_totals.append(int(option_player))
                    query_board.options_totals = json.dumps(options_totals)
                    query_board.save()

                ejemplo2 = copy_tabla

        #**********************************************
        # Luego de la insercion de cada movimiento se imprime la tabla con los jugadores

        data = {
            "id_sala": query_board.id,
            "board1": imprimir_tablero(ejemplo2)[0],
            "board2": imprimir_tablero(ejemplo2)[1],
            "board3": imprimir_tablero(ejemplo2)[2],
            "******": "******",
            f'player1 (X) id: {query_board.player1.id}': query_board.player1.username,
            f'player2 (O) id: {query_board.player2.id}': query_board.player2.username,
        }

        return Response(data=data)