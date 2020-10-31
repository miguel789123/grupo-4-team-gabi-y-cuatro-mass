
## **<center>Grupo 4: COMPUTACION GRÁFICA 1</center>**
### Datos Académicos

- **Universidad:** Universidad Nacional de San Antonio Abad del Cusco
- **Facultad:** Facultad de Ingeniería Eléctrica, Electrónica, Informática y Mecánica
- **Escuela Profesional:** Ingeniería Informática y de Sistemas

### Docente:
- **Quintanilla Portugal Roxana Lisette** [Roxana](https://github.com/nitanilla "Roxana")

### Tema:
 ****SPACE GAME en python****

### Colaboradores:
- **Gabriela Farfan Enriquez** [Gabi](https://github.com/gabrielafarfan1)
- **Miguel Angel Quispe Jimenes** [Miguel](https://github.com/miguel7891223 "Miguel")
- **JoseMaria Hanco** [JoseMaria](https://github.com/josemariahancco "JoseMaria")
- **Bryan Huillca Moso** [Bryan](https://github.com/BryanHuillcaMozo "Bryan")
- **Julinho Apaza Paredes** [Julinho](https://github.com/20julinho "Julinho")
---
### Implementado en:
- Lenguaje:  Python
[Obtener Python](https://www.python.org/downloads/)

### Herramientas:
- Python
- OpenGL
- Github, Git
- Sublimetext

## Introducción:
El proyecto de SPACE GAME nace a partir de una tarea del curso de GRÁFICA I, en el que se quiere poner en práctica lo aprendido en el plano 2D, para el cual se utilizó Python y openGL.

## Requisitos:
- Es recomendable tener conocimientos previos, de matemáticas sobretodo de geometría y de álgebra lineal.
- Un ordenador con conexión a internet para poder instalar todo el software y descargar el material.
- Es recomendable contar con conocimientos básicos de programación en python y openGL.

## Descripción
Bienvenidos al repositorio de "Gabi y 4 más" te invitamos a que revises el código de SPACE GAME. Este es un juego sencillo implementado en python y para ejecutar el juego, solo se debe descargar desde la opción en la parte superior que dice descargar como zip, o clonar el repositorio como se muestra en la sección Clonar Repositorio. Una vez hecho eso sería correr el archivo del juego necesario, generalmente terminado en extensión .py de la carpeta del juego deseado. A todos los que les guste la programación y quieran enfocarse al sector de videojuegos. Te esperamos!!!
[![nave](git "nave")](https://github.com/miguel789123/grupo-4-team-gabi/blob/main/nave%20espacial.png "nave")

### Documentación
- Empezamos diseñando los posibles personajes del juego. 
[![Nave Principal](GitHub "Nave Principal")](https://github.com/miguel789123/grupo-4-team-gabi/blob/main/nuestra_Navee.jpeg "Nave Principal") [![Nave Enemiga](GitHub "Nave Enemiga")](https://github.com/miguel789123/grupo-4-team-gabi/blob/main/nave_enemiga_posicion_2.jpeg "Nave Enemiga")[![Explosión](GitHub "Explosión")](https://github.com/miguel789123/grupo-4-team-gabi/blob/main/MatrizExplosion.jpg "Explosión")
- Definimos las idea principal del juego.
- Investigamos más sobre como de hacen juegos en python.
- Agregamos las funciones respectivas para graficar los monstros y la nave.
-	Cambiamos el diseño de los gráficos del juego.
-	Agregamos las funciones de movimiento en la nave.
-	Agregamos las funciones de movimiento en los monstruos.
-	Revisamos tutoriales en YouTube y documentación, para poder implementar la programación de eventos con la librería pygame.
-	Implementamos el control de movimiento mediante el teclado.
-	Implementamos las funciones de disparo.
-	Implementamos las funciones de colisión.
### Trabajo:
Elegimos un juego al que llamamos SPACE GAME
- Vamos a tener un main(principal), donde haremos uso de las librerías, definiremos nuestras funciones de colisión, reset game. Al igual que las variables vida, disco y los tiros.
- Se definió la clase invaders, en el cual graficamos mediante matrices a nuestra nave enemiga, en posición "1 y  2"; el disco, la explosión y la nave con la que jugaremos.
- Estos personajes se pintará pixel por pixel, cuando el valor de mp[i] [j]=1
- Se definió la clase shot, que ésta se hará uso para que la nave con la que jugaremos podra  disparar a las naves enemigas.
- Se definió la clase  shot_invaders la cual  se hará uso para que las naves enemigas, puedan disparar a nuestra nave con la que jugaremos.
- El juego inicia al presionar la tecla enter.
- Se dispara al presionar la tecla espacio.
- los comandos para mover nuestra nave será haciendo el uso de las flechas (<- y ->).
- La nave con la que jugaremos tiene 4 vidas.
- Para la nave enemiga se hará uso de for loops, esto para poder multiplicar nuestras naves enemigas. También vimos que se dibujó a la nave enemiga en dos posiciones, como están en las figuras (nave enemiga posición1 y nave enemiga posición 2), esto para poder intercambiar aleatoriamente "la nave enemiga posición 1 y nave enemiga posición 2" y se pueda ver en el juego que la nave enemiga se mueva aleteando y mostrando su cañon.
- Cuando la nave enemiga  reciba una bala(shot) de nuestra nave, se intercambiará la figura de la nave enemiga mostrando la explosión.
### Link del juego, publicado en youtube:
-https://www.youtube.com/watch?v=3zddwS7fRdM&feature=youtu.be
