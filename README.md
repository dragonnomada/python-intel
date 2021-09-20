# Curso de Python Intel

Por [Alan Badillo Salas (Dragón Nómada)](mailto://dragonnomada123@gmail.com)

Correo: [dragonnomada123@gmail.com](mailto://dragonnomada123@gmail.com)

## Noticias

* **Domingo 20 de Septiembre de 2021** - Ya está disponible la [Serie 4](./ejercicios/serie-4.md) de ejercicios.
* **Domingo 12 de Septiembre de 2021** - Ya está disponible la [Serie 3](./ejercicios/serie-3.md) de ejercicios.
* **Miércoles 8 de Septiembre de 2021** - Ya está disponible la [Serie 2](./ejercicios/serie-2.md) de ejercicios.

## Contenido

```text
> Módulo 1. Introducción a Python
¿Qué es Programación?
Escribir Código Fuente
Ejecutar Código Fuente
¿Por qué Python?
Instalando

> Módulo 2. Fundamentos de programación con Python
Variables
Tipos de Datos
Practicando los Tipos de Datos

> Módulo 3. Funciones, Números y Operadores
Funciones
Funciones con Parámetros y argumentos
Funciones que Retornan Valores
Diferencias entre Funciones y Métodos
Números y ejemplos con números
Funciones con Números

> Módulo 4. Arreglos e iteradores
Qué son los Arreglos (Arrays) en Programación
Trabajando con Lists en Python
Veamos que son los iteradores
```

> Sintaxis

```py
# Variable: 
#   <nombre> = <valor>
# Condicionales: 
#   if <condición>: 
#       <bloque>
#   elif <condición 2>:
#       <bloque 2> 
#   ... 
#   else: 
#       <bloque falso>
# Iteradores: 
#   for <elemento> in <secuencia>:
#       <bloque>
# Rangos: 
#   range(N) 1, 2, ... N - 1
#   range(a, b) a, a + 1, ..., b - 1
#   range(a, b, s) a, a + 1s, a + 2s, ..., b - 1
# Ciclos Condicionales: 
#   while <condición>:
#       <bloque> 
#       (break -> rompe)
#       (continue -> salta y continua)
# Funciones:
#   def <nombre>(<parámetros>):
#       <bloque>
#       (return -> regresa el cómputo/resultado)
```

## ¿Cómo clonar este repositorio?

> 1. Instalar Git para Windows (en Linux y Mac ya viene instalado)

[https://git-scm.com/download/win](https://git-scm.com/download/win)

> 2. En la terminal, ubicar la carpeta dónde se va a clonar

```bash
cd ~/Desktop
```

> 3. Clonar el repositorio

```bash
git clone https://github.com/dragonnomada/python-intel.git
```

> 4. Ir a la carpeta clonada (`python-intel`)

```bash
cd ~/Desktop/python-intel

--- terminal windows ---
dir

--- terminal windows / salida ---

Directorio: E:\santuario\cursos\python-intel


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        06/09/2021     20:24                codigos
d-----        06/09/2021     18:31                ejercicios
d-----        06/09/2021     18:43                lab
d-----        06/09/2021     20:23                notas
-a----        06/09/2021     20:54           1950 README.md
```

> 5. Abrir en Visual Code ([https://code.visualstudio.com](https://code.visualstudio.com))

```bash
code .
```

> 6. Para obtener los nuevos cambios

```bash
git pull
```