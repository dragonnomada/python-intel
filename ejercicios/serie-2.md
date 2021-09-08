# Ejercicios de Python - Serie II

By [Alan Badillo Salas (Dragón Nómada)](dragonnomada.medium.com)

## Introducción

En esta segunda serie de ejercicios nuestro objetivo será dominar la abstracción de código mediante funciones y terminar de entender la programación funcional.

## La tienda de frutas

En esta sección crearemos funciones útiles para administrar una tienda de frutas.

### S2E1 - Precio por fruta

Define una función llamada `precioFruta(<nombre>)` que devuelva el precio de la fruta dado el `<nombre>` de la fruta según la siguiente tabla de precios por kilo de fruta.

Fruta | Precio
--- | ---
`manzana` | 45
`mango` | 32
`pera` | 17
`guayaba` | 33
`melón` | 24
`papaya` | 16

> Pista - Define una función basado en la siguiente sintaxis

```py
def precioFruta(nombre):
    # TODO: Determina el precio dado el nombre de la fruta
```

> Pruebas unitarias - Ejecuta las siguientes pruebas

```
print( precioFruta("manzana") ) # 45
print( precioFruta("mango") ) # 32
print( precioFruta("melón") ) # 24
print( precioFruta() ) # None
print( precioFruta("manzana", "pera") ) # Error: Hay más argumentos de los esperados
```

### S2E2 - Precio por Lista de Frutas

Define una función llamada `precioListaFrutas(<lista frutas>)` que devuelva la suma de los precios de las frutas dadas en `<lista frutas>`, usando la función `precioFruta(<nombre>)` para calcular el precio de cada fruta a sumar. Considera que si el precio devuelto en `None` devuelvas `None` como resultado.

> Pista - Recorre cada fruta recibida en la lista. Cada fruta es el nombre de la fruta, por lo que debes recuperar su precio. Si el precio es `None` devuelve `None` como resultado de la función (usa `return None`). En otro caso, suma el precio a un acumulador de suma.

```py
# Recuerda como acumular una suma

s = 0

for <elemento> in <secuencia>:
    <valor> = ... # usa el <elemento> para calcular el valor
    s = s + <valor> # Calcula el <valor> como el precio de la fruta recorrida de la lista
```

> Pruebas unitarias - Ejecuta las siguientes pruebas

```py
print( precioListaFrutas(["manzana", "pera"]) ) # 62
print( precioListaFrutas(["manzana"]) ) # 45
print( precioListaFrutas(["pera"]) ) # 17
print( precioListaFrutas(["pera", "manzana"]) ) # 62
print( precioListaFrutas(["pera", "mango", "manzana"]) ) # 94
print( precioListaFrutas(["pera", "mango", "manzana", "papa"]) ) # None
print( precioListaFrutas([]) ) # 0
print( precioListaFrutas("manzana") ) # ¿Error o None?
```

### S2E3 - Precio de Frutas por Cantidad

Analiza el siguiente código y completa los `TODOs` marcados para obtener los precios por cantidad. Comenta que hace cada línea de código que no esté comentada.

```py
# Determina el precio de la fruta <nombre> según la <cantidad> de kilos que se compre
# Ejemplo: precioFrutaCantidad("manzana", 0.5) -> 22.5
def precioFrutaCantidad(nombre, cantidad):
    # Calcula el total llamando a la función `precioFruta(<nombre>)` multiplicado por la <cantidad>
    # Ejemplo: total = precioFruta("manzana") * 0.5 # total = 22.5
    total = precioFruta(nombre) * cantidad
    # Devuelve el total
    return total

# Devuelve los grupos de la fruta y la cantidad dada la <lista_fruta_cantidad>
# Ejemplo: gruposFrutaCantidad(["manzana", 0.5, "pera", 1.2, "mango", 0.3]) -> [["manzana", 0.5], ["pera", 1.2], ["mango", 0.3]]
def gruposFrutaCantidad(lista_fruta_cantidad):
    # Calcula el total de elementos de la <lista_fruta_cantidad>
    N = len(lista_fruta_cantidad)
    # Crea una lista vacía para guardar los grupos
    grupos = []
    # Recorre los índices de 0 a N-1 de 2 en 2 (es decir, 0, 2, 4, 6, ..., N-2)
    for i in range(0, N, 2):
        # Extrae la sublista (el grupo) cada 2 índices (ejemplo, ["manzana", 0.5] para el índce 0)
        grupo = lista_fruta_cantidad[i:i+2] # [0:2], [2:4], [4:6], ..., [N-2:N]
        # Agrega el grupo a los grupos
        grupos.append(grupo) # Ejemplo, ["manzana", 0.5] | ["pera", 1.2] | ["mango", 0.3]
    return grupos

def precioListaFrutaCantidad(lista_fruta_cantidad):
    grupos = gruposFrutaCantidad(lista_fruta_cantidad)
    # TODO: Declara un acumulador para almacenar la suma de los totales (ejemplo, `suma_totales = 0`)
    for grupo in grupos:
        nombre = ... # TODO: Obtén el valor del `grupo` en la posición 0
        cantidad = ... # TODO: Obtén el valor del `grupo` en la posición 1
        total = ... # Calcula el total llamando a la función `precioFrutaCantidad(...)`
        # TODO: Acumula a la suma el total
    # TODO: Devuelve la suma de los totales acumulados
```

> Pista - El código anterior define tres funciones explicadas en la siguiente tabla

Función | Explicación
--- | ---
`precioFrutaCantidad(nombre, cantidad)` | Recibe el `<nombre>` de la fruta y la `<cantidad>` y devuelve el precio de la fruta según la cantidad, por ejemplo, `precioFrutaCantidad("melón", 0.25) -> 6.0`
`gruposFrutaCantidad(lista_fruta_cantidad)` | Toma una `<lista_fruta_cantidad>` y agrupa de 2 en 2, por ejemplo, `gruposFrutaCantidad(["manzana", 0.5, "pera", 1.2]) -> [["manzana", 0.5], ["pera", 1.2]]`
`precioListaFrutaCantidad(lista_fruta_cantidad)` | Toma una `<lista_fruta_cantidad>` y devuelve la suma de los totales para cada pareja, por ejemplo, `precioListaFrutaCantidad(["manzana", 0.5, "pera", 1.2]) -> 42.9`

* **Nota:** La última función no está comentada ni funciona, así que tendrás que comentar que hace cada línea de código y resolver lo que está marcado en los `TODOs`.

> Pruebas unitarias - Ejecuta las siguientes pruebas

```py
print( precioFrutaCantidad("manzana", 0.5) ) # 22.5
print( precioFrutaCantidad("pera", 1.2) ) # 20.4
print( precioFrutaCantidad("mango", 0.3) ) # 9.6

print( gruposFrutaCantidad(["manzana", 0.5, "pera", 1.2]) ) # [["manzana", 0.5], ["pera", 1.2]]
print( gruposFrutaCantidad(["pera", 1.2, "manzana", 0.5]) ) # [["pera", 1.2], ["manzana", 0.5]]
print( gruposFrutaCantidad(["pera", 1.2, "mango", 0.3, "manzana", 0.5]) ) # [["pera", 1.2], ["mango", 0.3], ["manzana", 0.5]]

print( precioListaFrutaCantidad(["manzana", 0.5, "pera", 1.2]) ) # 42.9
print( precioListaFrutaCantidad(["pera", 1.2, "manzana", 0.5]) ) # 42.9
print( precioListaFrutaCantidad(["pera", 1.2, "mango", 0.3, "manzana", 0.5]) ) # 52.5

lista_fruta_cantidad = []

for fruta in ["manzana", "pera", "mango", "papaya"]:
    cantidad = float( input("Dame la cantidad de kilos a comprar de la fruta {}".format(fruta)) )
    lista_fruta_cantidad.append(fruta, cantidad)

print("Se comprarán las siguientes frutas: {}", gruposFrutaCantidad(lista_fruta_cantidad))
print("El total es de: ${:.2f}", precioListaFrutaCantidad(lista_fruta_cantidad))
```