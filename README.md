# DESAFIO PINTAR TABLERO DE AJEDREZ

## Tabla de contenido
1. [Información general](#información-general)
2. [Tecnologías](#tecnologías)
3. [Razonamiento y Solución](#razonamiento y solución)
4. [Capturas de Pantalla](#capturas de pantalla)

### Información general
***
Desafío para la empresa Recruitingmsa. 

Planteo: Un niño está jugando a colorear su tablero de ajedrez y va a pintar cada casilla toda de azul o toda de rojo. Para darle un toque personalizado, quiere pintar la misma cantidad de casillas rojas que de azules, pero no quiere que le queden dos columnas con la misma cantidad de casillas rojas pintadas, ni quiere que le queden dos filas con la misma cantidad de casillas rojas pintadas.

¿Puede lograr pintarlo cumpliendo esas condiciones?

¿Y si en vez de un tablero de ajedrez normal de 8x8 fuese un tablero de ajedrez gigante de 1000x1000?

## Tecnologías
***
Una lista de tecnologías utilizadas en el proyecto:
* [Python](https://python.com): Versión 3.10.4
* [Tkinter](https://docs.python.org/es/3/library/tkinter.html): Version 8.5
* [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter): Version 4.3

## Razonamiento y Solución
***
Utilicé el lenguaje de programación python por que es el que mas domino actualmente, y con el cual tengo mas experiencia.
Ya había utilizado la librería tkinter para desarrollo de interfaces graficas muy buena para software de escritorio, asi que elegí este camino para resolver el desafío. Como un plus utilicé la librería Custom-Tkinter desarrolada por TomSchimansky la cual le da un toque moderno e incluí funcionalidad para cambiar color de tema de la App.

Como el planteo pide pintar un tablero 8x8 y luego desafia a hacer uno de 1000x1000, decidí hacer una app que pudiese crear ambos casos, y de paso agregue otra opcion que sería un tablero de 100x100 y la posibilidad de seleccionar los colores entre 6 opciones de color.
Para dibujar el mismo utilicé el widget de tkinter "Canvas" ya que en primer lugar pensaba pintar la pantalla con "Labels" pero esto produjo problemas cuando el tablero se hacía mas grande y se trababa la App. Con Canvas mejoró mucisimo pero con el tablero de 1000x1000 tarda unos 6 segundos en mi PC y se tilda un poco cuando se hace Scroll para ver el tablero.
El dibujo de cada casillero se realiza con un bucle for anidado el cual contiene un if para hacer que se cumplan las condiciones de color.

Espero les agrade mi solución, desde ya aclaro que no tengo mucha experiencia pero si deceo de aprender constantemente sobre programación ya que me apaciona y quiero trabajar de esto. Saludos.


### Capturas de pantalla
![Principal](https://i.ibb.co/XD1p1WP/desafio-Ajedrez.gif)
