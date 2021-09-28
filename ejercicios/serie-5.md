# Ejercicios de Python - Serie V

By [Alan Badillo Salas (Dragón Nómada)](dragonnomada.medium.com)

## Introducción

En esta quinta serie dominaremos la creación y uso de clases y objetos, para así entender los conceptos de la programación orientada a objetos.

## Diseño de Clases

### S5D1 - El objeto fruta

Crea una clase llamada `Fruta` que contenga los atributos y métodos descritos en la siguiente tabla.

Tipo | Nombre | Dato / Parámetros | Descripción
--- | --- | --- | ---
Atributo | `nombre` | `str` | Nombre de la fruta (por defecto `""`)
Atributo | `precio` | `float` | Precio de la fruta (por defecto `0.0`)
Atributo | `cantidad` | `int` | Cantidad de esa fruta (por defecto `0`)
Método | `describir` | `(self)` | Imprime con formato `"Fruta {} ${.2f} ({})".format(self.nombre, self.precio, self.cantidad)`
Método | `setNombre` | `(self, nombre)` | Ajusta el nombre
Método | `setNombre` | `(self, precio)` | Ajusta el precio
Método | `setNombre` | `(self, cantidad)` | Ajusta la cantidad
Método | `estaDisponible` | `(self)` | Devuelve un booleano si la cantidad es mayor a cero
Método | `precioValido` | `(self)` | Devuelve si el precio es mayor a uno

> Pruebas de validación

```py
fruta = Fruta()

fruta.setNombre("manzana")
fruta.setPrecio(10.5)
fruta.setCantidad(2)


if fruta.estaDisponible() and fruta.precioValido(): # True and True
    fruta.describir() # Se imprime "Fruta manzana $10.50 (2)"
```

### S5D2 - El objeto Reporte

Completa la clase llamada `Reporte` que implemente las funcionalidades descritas en `# TODO`.

> Clase Reporte

```py
class Reporte:
    columnas = []
    datos = {}

    def agregarColumna(self, columna):
        # TODO: Agrega `columna` a la lista `self.columnas`

    def agregarDato(self, nombre, valor):
        # TODO: Agrega la clave `nombre` y el `valor` al diccionario `self.datos`

    def imprimir(self):
        # Supongamos que:
        # `self.columnas = ["nombre", "edad", "esCasado"]`
        # `self.datos = { "nombre": "Ana", "edad": 23, "esCasado": False }`
        
        # TODO: Imprime todas las columnas con el formato `| {:10} | {:10} | ... |` para cada columna
        # Ejemplo: | nombre | edad | esCasado |
        
        # TODO: Imprime todos los datos para cada columna `| {:10} | {:10} | ... |` para cada columna
        # Ejemplo: | Ana | 23 | False |
```

> Pruebas unitarias

```py
reporte = Reporte()

reporte.agregarColumna("Nombre")
reporte.agregarColumna("Edad")
reporte.agregarColumna("EsCasado")

reporte.agregarDato("Nombre", "Ana")
reporte.agregarDato("Edad", 23)
reporte.agregarDato("Nombre", False)

reporte.imprimir()
# Imprime:
# | Nombre     | Edad       | EsCasado   |
# | Ana        | 23         | False      |
```

### S5D3 - Piedra Papel o Tijeras

Crea las clases `Piedra`, `Papel`, `Tijeras` con el atributo `nombre` con `PIEDRA`, `PAPEL` o `TIJERAS` (según la clase) y el método `comparar(jugada)`, dónde `jugada` sea una instancia de `Piedra`, `Papel` o `Tijera` (revisa la prueba unitaria). El método `comparar(jugada)` deberá devolver `1` si la clase le gana a la otra, `-1` si pierde y `0` si es empate.

> Pruebas unitarias

```py
jugada1 = Piedra()
jugada2 = Tijeras()

if jugada1.comparar(jugada2) == 1:
    print(f"Gana Jugada 1 vs Jugada 2: {jugada1.nombre} le gana a {jugada2.nombre}") # Si se imprime

if jugada2.comparar(jugada1) == -1:
    print(f"Pierde Jugada 2 vs Jugada 1: {jugada2.nombre} pierde contra {jugada1.nombre}") # Si se imprime

jugada3 = Papel()

if jugada1.comparar(jugada3) == -1:
    print(f"Pierde Jugada 1 vs Jugada 3: {jugada1.nombre} pierde contra {jugada3.nombre}") # Si se imprime

if jugada3.comparar(jugada2) == 1:
    print(f"Pierde Jugada 3 vs Jugada 2: {jugada3.nombre} le gana a {jugada2.nombre}") # Si se imprime

jugada4 = Tijeras()

if jugada4.comparar(jugada2) == 0:
    print(f"Empata Jugada 4 vs Jugada 2: {jugada4.nombre} es igual que {jugada2.nombre}") # Si se imprime

if jugada2.comparar(jugada4) == 0:
    print(f"Empata Jugada 2 vs Jugada 4: {jugada2.nombre} es igual que {jugada4.nombre}") # Si se imprime
```
