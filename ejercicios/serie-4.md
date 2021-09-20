# Ejercicios de Python - Serie IV

By [Alan Badillo Salas (Dragón Nómada)](dragonnomada.medium.com)

## Introducción

En esta cuarta serie de ejercicios dominaremos el uso de archivos de texto.

## Lectura de Archivos

### S4R1 - Leer frutas

Crea un archivo de texto llamado `frutas.txt` que contenga el nombre de una fruta por cada línea del archivo, como se muestra en el ejemplo. Recupera cada fruta e imprime el número de línea y el nombre de la fruta con el formato `{num_linea}. Fruta: {nombre}`.

> Ejemplo del archivo `frutas.txt`

```txt
manzana
pera
mango
kiwi
guayaba
```

> Ejemplo de la salida

```txt
1. Fruta: manzana
2. Fruta: pera
3. Fruta: mango
4. Fruta: kiwi
5. Fruta: guayaba
```

### S4R2 - Leer frutas y cantidades

Crea un archivo de texto llamado `frutas_cantidades.txt` que contenga el nombre de una fruta, un espacio en blanco y una cantidad decimal por cada línea del archivo, como se muestra en el ejemplo. Recupera cada línea del archivo y separa sus partes por el separador espacio. Imprime el nùmero de línea, el nombre de la fruta y la cantidad multiplicada por `1,000` con el formato `{num_linea}. Fruta: {nombre} Cantidad: {cantidad}`.

> Ejemplo del archivo `frutas_cantidades.txt`

```txt
manzana 10
pera 5
mango 0.001
kiwi 0.3
guayaba 1000
```

> Ejemplo de la salida

```txt
1. Fruta: manzana Cantidad: 10000
2. Fruta: pera Cantidad: 5000
3. Fruta: mango Cantidad: 1
4. Fruta: kiwi Cantidad: 300
5. Fruta: guayaba Cantidad: 1000000
```

### S4R3 - Leer Torneos

Crea un archivo llamado `torneo.txt` que contenga en la primer línea el número de jugadores `N` que pelearan, en las siguientes `N` líneas lee el nombre de cada jugador. Pasando las `N` líneas, lee el número de batallas (`B`) que pelearan dos jugadores, luego en las siguientes `B` líneas recupera los identificadores del primer y segundo jugador. Imprime un mensaje por cada pantalla con el formato `Batalla {num_batalla}: Pelea {nombre_jugador_1} vs {nombre_jugador_2}`. Revisa el ejemplo de abajo.

> Ejemplo del archivo `torneo.txt`

```txt
4
Ana
Paco
Pepe
Lisa
6
1 2
3 4
2 3
3 1
1 4
4 2
```

> Ejemplo de salida

```txt
Batalla 1: Pelea Ana vs Paco
Batalla 2: Pelea Pepe vs Lisa
Batalla 3: Pelea Paco vs Pepe
Batalla 4: Pelea Pepe vs Ana
Batalla 5: Pelea Ana vs Lisa
Batalla 6: Pelea Lisa vs Paco
```

> Pista: Sigue el siguiente pseudocódigo para guiarte

```txt
INICIO

f <- LEER ARCHIVO `torneo.txt` EN MODO LECTURA

N <- CONVIERTE A ENTERO: LEER LINEA DE ARCHIVO f

Jugadores <- LISTA VACIA

PARA n EN RANGO DE N:
    nombre_jugador <- LEER LINEA DE ARCHIVO f
    AGREGAR nombre_jugador A LISTA Jugadores

B <- CONVIERTE A ENTERO: LEER LINEA DE ARCHIVO f

PARA b EN RANGO DE B:
    batalla <- LEER LINEA DE ARCHIVO f
    
    partes_batalla <- batalla SEPARAR POR ESPACIO
    
    jugador_1 <- CONVIERTE A ENTERO: partes_batalla EN INDICE 0
    jugador_2 <- CONVIERTE A ENTERO: partes_batalla EN INDICE 1

    nombre_jugador_1 <- LISTA Jugadores EN INDICE (jugador_1 - 1) # Índices empiezan en 0
    nombre_jugador_2 <- LISTA Jugadores EN INDICE (jugador_2 - 1) # Índices empeizan en 0

    IMPRIMIR CON FORMATO "Batalla {b + 1}: Pelea {nombre_jugador_1} vs {nombre_jugador_2}"

CIERRA ARCHIVO f
```

## Escritura de Archivos

### S4W1 - Escribir los nombres y su longitud

Crea una lista con nombres como `["Ana", "Pepe", "Paco", "Lisa"]`. Escribe el archivo `nombres.txt` con cada nombre, un espacio en blanco y su longitud (usa `len(nombre)` para obtenerla).

> Ejemplo del archivo creado `nombres.txt`

```txt
Ana 3
Pepe 4
Paco 4
Lisa 4
```

### S4W2 - Escribir las frutas y sus cantidades

Crea un diccionario de frutas como `{ "manzana": 10, "pera": 5, "kiwi": 0.1, "guayaba": 0.08 }`. Escribe el archivo llamado  `frutas_diccionario.txt` con cada clave (nombre de la fruta), un espacio en blanco y el valor (la cantidad) multiplicada por `100`. Prueba iterar con `for nombre, cantidad in frutas.items()`.

> Ejemplo del archivo creado `frutas_diccionario.txt`

```txt
manzana 1000
pera 500
kiwi 10
guayaba 8
```

### S4W3 - Escribir un archivo cada 5 segundos

Crea un ciclo indeterminado que en cada iteración abra el archivo `logs.txt` y escriba la fecha actual en formato **ISO 8601** y el archivo `log_{fecha_actual_iso2}.txt` que contenga el texto `HOLA MUNDO`. Revisa los ejemplos de abajo. Espera 5 segundos antes de la próxima iteración y no olvides cerrar el archivo.

**Nota**: Reemplaza los caracteres `:` por `_` en la `fecha_actual_iso` mediante `fecha_actual_iso2 = fecha_actual_iso.replace(":", "_")` para que se pueda escribir el archivo.

> Ejemplo del archivo `logs.txt`

```txt
2021-09-20T12:00:00.0000
2021-09-20T12:00:05.0000
2021-09-20T12:00:10.0000
```

> Ejemplo del archivo `log_2021-09-20T12_00_00.0000`

```txt
HOLA MUNDO
```

> Ejemplo del archivo `log_2021-09-20T12_00_05.0000`

```txt
HOLA MUNDO
```

> Ejemplo del archivo `log_2021-09-20T12_00_10.0000`

```txt
HOLA MUNDO
```


> Pista: Generar la fecha actual en formato iso

```py
from datetime import datetime
fecha_actual_iso = datetime.now().isoformat()
print(fecha_actual_iso)
```