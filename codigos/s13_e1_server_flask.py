from flask import Flask # 1.1.2

app = Flask(__name__)

@app.get("/") # locahost:5000/
def home():
    return "Hola Flask"

@app.get("/api/productos") # locahost:5000/api/productos
def get_productos():
    productos = [
        {
            "nombre": "Coca Cola",
            "precio": 16.5
        },
        {
            "nombre": "Galletas",
            "precio": 18.99
        },
    ]
    return {
        "productos": productos
    }

app.run() # localhost:5000