# pip install turtle

# https://docs.python.org/es/3/library/turtle.html

# turtle.forward(<distance>) - Avanza la distancia
# turtle.backward(<distance>) - Retrocede la distancia
# turtle.right(<angle>) - Gira la cabeza el ángulo en sentido horario
# turtle.left(<angle>) - Gira la cabeza el ángulo en sentido anti-horario
# turtle.penup() - Levanta el lápiz (deja de dibujar)
# turtle.pendown() - Baja el lápiz (comienza a dibujar mientras avanza)

import turtle
import math

turtle.penup()
turtle.right(120)
turtle.forward(100)
turtle.left(150)

C = (100 ** 2 + 100 ** 2 - 2 * 100 * 100 * math.cos(120 * math.pi / 180)) ** 0.5

turtle.pencolor("#857743")
turtle.pendown()
turtle.forward(C)
turtle.left(120)
turtle.forward(C)
turtle.left(120)
turtle.forward(C)

turtle.Screen().exitonclick()