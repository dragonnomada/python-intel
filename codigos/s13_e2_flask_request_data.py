from flask import Flask
from flask import request

app = Flask(__name__)

@app.get("/") # locahost:5000/
def home():
    return "Hola Flask"

@app.get("/api/productos") # locahost:5000/api/productos?min_precio=<float>
def get_productos():
    min_precio = request.args.get("min_precio")
    
    if not min_precio:
        min_precio = 0
    else:
        min_precio = float(min_precio)
    
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
    
    productos_filtrados = [ producto for producto in productos if producto["precio"] >= min_precio ]
    
    return {
        "productos": productos_filtrados
    }

app.run() # localhost:5000