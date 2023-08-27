import os

#***********************************************
#******************VARIABLES********************

finish_game = 0
option_game = 0

options_player1 = []
options_player2 = []
options_totals = []

player1_win = False
player2_win = False

tablero = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
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

#************************************************
#*************FUNCIONES**************************


def limpiar_pantalla():
    os.system('clear')


def verificar_ganador(options_win, options_player):
    for reg in options_win:
        if set(reg).issubset(options_player):
            player_win = True
            return player_win


def input_number(name_jugador, options_totals, tablero, indicador):
    while True:
        print(" ")
        print(f'***  Digite el numero de la casilla para poner la ("{indicador}")  ***')
        print(" ")
        print(f'Turno de {name_jugador}:')
        entrada = input()
        if entrada.isdigit():
            if int(entrada) not in options_totals and 0 < int(entrada) < 10:
                return int(entrada)
        limpiar_pantalla()
        imprimir_tablero(tablero)
        print(" ")
        print("******************************************")
        print("Por favor, ingresa un numero diferente....")
        print("******************************************")
        print(" ")


def imprimir_tablero(tablero):
    for fila in tablero:
        print("|".join(map(str, fila)))
        print("-" * 5)


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


def menu():
    limpiar_pantalla()
    print("*************** MENU *******************")
    print("*************TIC_TAC_TOE****************")
    print("****************************************")
    print(" ")
    print("1. Jugar")
    print("2. Salir")


#********************************
#***********MAIN*****************

while finish_game < 1:

    # Se realiza un menu para que al momento de que acabe el juego se 
    # Regrese a esté

    menu()
    print(" ")
    print("Digite la opcion: ")
    op = input()
    if op.isdigit():
        if int(op) == 2:
            print(" ")
            print("Ha salido del juego con exito...")
            finish_game = 1
            break

    #Pido los datos del nombre de usuario
            
    limpiar_pantalla()
    name_player1 = input("Ingresa el nombre del Jugador 1: ")
    limpiar_pantalla()
    name_player2 = input("Ingresa el nombre del Jugador 2: ")

    count_game = 1

    limpiar_pantalla()

    # En este while mientras que el numero de jugadas totales no sea mayor a 9
    # El juego no se acabara

    while count_game < 9:

        count_game += 1

        # Se valida si la lista de movimientos totales tiene los 9 movimientos
        # permitidos para determinar un empate

        if len(options_totals) > 8:
            count_game = 10
            break

        imprimir_tablero(tablero)

        # Pedimos el movimiento que hará el jugador luego de esto
        # Insertó el movimiento y lo agrego en la lista de movimientos del jugador
        # Tambien lo inserto en la tabla de movimientos totales
        # Luego de esto valido si con las opciones que el jugador ha realizado
        # A ganado o la partida sigue

        opt_player_1 = input_number(name_player1, options_totals, tablero, "X")
        match_tablero(opt_player_1, tablero, "X")
        options_player1.append(opt_player_1)
        options_totals.append(opt_player_1)
        player1_win = verificar_ganador(options_win, options_player1)
        if player1_win:
            count_game = 9
            break

        limpiar_pantalla()

        if len(options_totals) > 8:
            count_game = 10
            break

        imprimir_tablero(tablero)

        # Pedimos el movimiento que hará el jugador luego de esto
        # Insertó el movimiento y lo agrego en la lista de movimientos del jugador
        # Tambien lo inserto en la tabla de movimientos totales
        # Luego de esto valido si con las opciones que el jugador ha realizado
        # A ganado o la partida sigue

        opt_player_2 = input_number(name_player2, options_totals, tablero, "O")
        match_tablero(opt_player_2, tablero, "O")
        options_player2.append(opt_player_2)
        options_totals.append(opt_player_2)
        player2_win = verificar_ganador(options_win, options_player1)
        if player2_win:
            count_game = 9
            break


        limpiar_pantalla()

    # Imprimir resultados

    # En la funcion anterior verificar si el jugador gano
    # Sí ganó se cambia el estado de la variable 'player1_win' a true
    # Luego entra a la siguiente validacion y lo declara ganador

    if player1_win:
        limpiar_pantalla()
        imprimir_tablero(tablero)
        print(" ")
        print(f'¡Ganador {name_player1}!')
        print(" ")
        enter = input("Presione 'Enter' para volver al menu ...")

    # En la funcion anterior verificar si el jugador gano
    # Sí ganó se cambia el estado de la variable 'player2_win' a true
    # Luego entra a la siguiente validacion y lo declara ganador

    elif player2_win:
        limpiar_pantalla()
        imprimir_tablero(tablero)
        print(" ")
        print(f'¡Ganador {name_player2}!')
        print(" ")
        enter = input("Presione 'Enter' para volver al menu ...")

    # Si ninguna de las dos validaciones se cumple declara el juego como en empate

    else:
        limpiar_pantalla()
        imprimir_tablero(tablero)
        print("Empate ____****")
        print("  ")
        enter = input("Presione 'Enter' para volver al menu ...")
