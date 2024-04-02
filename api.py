from flask import Flask, request, jsonify
from pymongo import MongoClient
import random
import string

app = Flask(__name__)

# Configuración de la conexión a la base de datos MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mi_base_de_datos']
collection = db['datos']

# Método GET para obtener datos aleatorios en formato JSON
@app.route('/datos', methods=['GET'])
def obtener_datos():
    datos = {
        'precio': str(random.randint(1, 100)),
        'nombre': ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)),
        'fecha': ''.join(random.choices(string.ascii_lowercase, k=5)),
        'url': 'https://www.ejemplo.com/' + ''.join(random.choices(string.ascii_lowercase, k=5))
    }
    return jsonify(datos)

# Método POST para almacenar datos en la base de datos MongoDB
@app.route('/datos', methods=['POST'])
def almacenar_datos():
    nuevo_dato = request.json
    collection.insert_one(nuevo_dato)
    return jsonify({'mensaje': 'Datos almacenados correctamente'}), 201

if __name__ == '__main__':
    app.run(debug=True)