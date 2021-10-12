from flask import Flask, render_template
import random

app = Flask(__name__)

@app.get("/")
def get_home():
    return render_template("index.html")

@app.get("/clima")
def get_clima():
    # TODO: Obtener los valores actuales del clima
    
    temperatura = random.uniform(0, 38)
    humedad = random.uniform(20, 98)
    
    ciudades = [
        {
            "nombre": "CDMX",
            "temperatura": random.uniform(17, 27),
            "humedad": random.uniform(45, 67)
        },
        {
            "nombre": "Monterrey",
            "temperatura": random.uniform(26, 42),
            "humedad": random.uniform(20, 50)
        },
        {
            "nombre": "Guadalajara",
            "temperatura": random.uniform(20, 30),
            "humedad": random.uniform(50, 70)
        },
    ]
    
    return render_template("clima.html", temperatura=temperatura, humedad=humedad, ciudades=ciudades)

app.run()

