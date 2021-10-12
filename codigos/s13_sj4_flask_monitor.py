from flask import Flask
from threading import Thread
from time import sleep
import random

context = {
    "on": True,
    "temperatura": 0,
    "humedad": 0,
    "distancia_1": 0,
    "distancia_2": 0,
    "rotacion_x": 0,
    "rotacion_y": 0,
    "rotacion_z": 0,
}

def read_sensors():
    while context["on"]:
        context["temperatura"] = random.uniform(0, 50)
        context["humedad"] = random.uniform(0, 100)
        context["distancia_1"] = random.uniform(0, 200)
        context["distancia_2"] = random.uniform(0, 200)
        context["rotacion_x"] = random.uniform(-90, 90)
        context["rotacion_y"] = random.uniform(-90, 90)
        context["rotacion_z"] = random.uniform(-90, 90)
        sleep(10)

app = Flask(__name__)

t = Thread(target=read_sensors)

t.start()

@app.get("/api/sensors")
def get_sensors():
    return context

app.run()

t.join()