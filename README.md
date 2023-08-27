
# TicTacToe

El proyecto es un juego inspirado en el clásico Tic Tac Toe. Se ha implementado tanto como una aplicación de línea de comandos (CLI) como a través de una API REST para consumo. Se puede jugar ya sea en la versión CLI o a través de la API REST.


## Pre-requisitos 📋

Instalar las dependencias mediante el archivo requirements.txt, copie el siguiente comando y lo pega en la terminal.

<!--sec data-title="Current directory: OS X and Linux" data-id="OSX_Linux_pwd" data-collapse=true ces-->

{% filename %}command-line{% endfilename %}

    pip install -r requirements.txt
    

> Nota: Este comando instala los requerimientos necesarios para el funcionamineto del proyecto.

<!--endsec-->

<!--sec data-title="Current directory: Windows" data-id="windows_cd" data-collapse=true ces-->

Verifique antes que usted se ubique en la ruta del proyecto donde este el archivo.


## Funcionamiento por medio del CLI

Antes de usar el comando para correr el proyecto por medio del CLI debe verificar que este en la ruta donde se encuentra el archivo .py

```
 > prueba.py
```

Luego de saber de que este en la ruta donde se encuentra el archivo, pegar en la terminal el siguiente comando para arrancar el proyecto



<!--sec data-title="Current directory: OS X and Linux" data-id="OSX_Linux_pwd" data-collapse=true ces-->

{% filename %}command-line{% endfilename %}

    python prueba.py

> Nota: Este comando inicia el juego por el CLI

<!--endsec-->

<!--sec data-title="Current directory: Windows" data-id="windows_cd" data-collapse=true ces-->


## Funcionamiento por medio de API Rest

Verifique que este en la ruta del proyecto donde este ubicado el archivo manage.py

```
 > manage.py
```

Luego de que haya verificado que este en la ruta, utilizar el comando para crear las migraciones y luego de esto aplicar las migraciones

<!--sec data-title="Current directory: OS X and Linux" data-id="OSX_Linux_pwd" data-collapse=true ces-->

{% filename %}command-line{% endfilename %}

    python manage.py makemigrations

{% filename %}command-line{% endfilename %}

    python manage.py migrate

<!--endsec-->

<!--sec data-title="Current directory: Windows" data-id="windows_cd" data-collapse=true ces-->

Luego de que haya migrato realizado el comando de las migraciones ya puede utilizar el comando para correr el proyecto

<!--sec data-title="Current directory: OS X and Linux" data-id="OSX_Linux_pwd" data-collapse=true ces-->

{% filename %}command-line{% endfilename %}

    python manage.py runserver

<!--endsec-->

<!--sec data-title="Current directory: Windows" data-id="windows_cd" data-collapse=true ces-->


## Como utilizar las API's para jugar

Para empezar a jugar antes hay que crear un tablero con los jugadores que van a estar en la partida


#### Recomendaciones 📝

Para ver la respuesta de las API rest podemos utilizar un conversor que lo muestre de una manera más estetica y entendible

* [JSON Formatter](https://jsonformatter.curiousconcept.com/#) - Usado para formatear y validar un JSON


### Crear tablero para jugar

Para crear la partida debemos utlizar el siguiente comando consumir el endpoint en la terminal...


<!--sec data-title="Current directory: OS X and Linux" data-id="OSX_Linux_pwd" data-collapse=true ces-->

{% filename %}command-line{% endfilename %}

    curl -X POST -H "Content-Type: application/json" -d '{"username_player1": "1", "username_player2": "1"}' "http://localhost:8000/api/v1/board_game/create/"

> Nota: Este comando tiene datos de ejemplo, tiene que poner los datos que desea en las variables de nombre

<!--endsec-->

<!--sec data-title="Current directory: Windows" data-id="windows_cd" data-collapse=true ces-->

Luego de esto la api respondera mediente un json con los datos del id de la sala, del jugador 1 y del jugador 2

```
{"board1":"1|2|3","board2":"4|5|6","board3":"7|8|9","player1":"1, vas a jugar con el id #5","player2":"1, vas a jugar con el id #5","sala":"El numero del tablero es: 4"}
```

```
{
   "board1":"1|2|3",
   "board2":"4|5|6",
   "board3":"7|8|9",
   "player1":"1, vas a jugar con el id #5",
   "player2":"1, vas a jugar con el id #5",
   "sala":"El numero del tablero es: 4"
}
```

> Nota : Este es la respuesta del JSON utilizando la pagina de [JSON Formatter]


### Traer el tablero

Para traer el tablero se realiza por mediante un enpoint get, el cual trae el tablero con los movimientos que se han realizado

<!--sec data-title="Current directory: OS X and Linux" data-id="OSX_Linux_pwd" data-collapse=true ces-->

{% filename %}command-line{% endfilename %}

    curl http://localhost:8000/api/v1/board_game/list/1/

> Nota: Este comando tiene datos de ejemplo, tiene poner al final del enpoint el id del tablero que desea observar

<!--endsec-->

<!--sec data-title="Current directory: Windows" data-id="windows_cd" data-collapse=true ces-->

La API respondera con el siguiente JSON...

```
{"board1":"X|X|3","board2":"4|O|X","board3":"O|8|9","******":"******","player1 (X) id: 1":"luigi","player2 (O) id: 2":"paco"}
```

```
{
   "board1":"X|X|3",
   "board2":"4|O|X",
   "board3":"O|8|9",
   "******":"******",
   "player1 (X) id: 1":"luigi",
   "player2 (O) id: 2":"paco"
}
```
> Nota : Este es la respuesta del JSON utilizando la pagina de [JSON Formatter]


### Crear turno de jugador

Este endpoint se utiliza para crear el turno de un jugador, se agrega el id del jugador, de la sala y la posicion en la que quiere jugar, se realiza un metodo POST

<!--sec data-title="Current directory: OS X and Linux" data-id="OSX_Linux_pwd" data-collapse=true ces-->

{% filename %}command-line{% endfilename %}

    curl -X POST -H "Content-Type: application/json" -d '{"id_player": "1", "id_sala": "1", "option_player": "1"}' "http://localhost:8000/api/v1/board_game/turn_create/

> Nota: Este comando tiene datos de ejemplo, en la data que se va a enviar en el endpoint, hay que poner id del jugador, id de la sala, y la posicion en la que quiere jugar

<!--endsec-->

<!--sec data-title="Current directory: Windows" data-id="windows_cd" data-collapse=true ces-->


> Example:
```
 {
   "id_player":"1",
   "id_sala":"1",
   "option_player":"1"
}
```

La respuesta de este endpoint será algo parecido a esto...

```
{"id_sala":1,"board1":"X|X|3","board2":"4|O|X","board3":"O|8|9","******":"******","player1 (X) id: 1":"luigi","player2 (O) id: 2":"paco"
```

```
{
   "id_sala":1,
   "board1":"X|X|3",
   "board2":"4|O|X",
   "board3":"O|8|9",
   "******":"******",
   "player1 (X) id: 1":"luigi",
   "player2 (O) id: 2":"paco"
}
```
> Nota : Este es la respuesta del JSON utilizando la pagina de [JSON Formatter]


## ¿Listo?
¡Vamos a bucear en Python!