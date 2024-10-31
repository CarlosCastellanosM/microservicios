from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os
import requests

# Cargar variables de entorno
load_dotenv()

# Inicializar la aplicación Flask
app = Flask(__name__)

# Datos simulados de pedidos
pedidos = [
    {"id": 1, "usuario_id": 1, "producto": "Laptop", "cantidad": 1},
    {"id": 2, "usuario_id": 2, "producto": "Monitor", "cantidad": 2}
]

# Función para verificar si un usuario es válido
def verificar_usuario(usuario_id):
    try:
        response = requests.get(f'http://localhost:{os.getenv("USERS_SERVICE_PORT")}/api/usuarios/{usuario_id}')
        return response.status_code == 200
    except requests.RequestException:
        return False

# Ruta para obtener todos los pedidos
@app.route('/api/pedidos', methods=['GET'])
def obtener_pedidos():
    return jsonify({
        "servicio": "pedidos",
        "data": pedidos,
        "status": "success"
    })

# Ruta para obtener los pedidos de un usuario específico
@app.route('/api/pedidos/<int:usuario_id>', methods=['GET'])
def obtener_pedidos_usuario(usuario_id):
    if not verificar_usuario(usuario_id):
        return jsonify({"error": "Usuario no válido", "status": "error"}), 404
    
    pedidos_usuario = [p for p in pedidos if p['usuario_id'] == usuario_id]
    return jsonify({
        "servicio": "pedidos",
        "data": pedidos_usuario,
        "status": "success"
    })

# Ruta para verificar la salud del servicio
@app.route('/api/pedidos/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({"status": "healthy", "service": "pedidos"})

# Ejecución de la aplicación
if __name__ == '__main__':
    port = int(os.getenv('ORDERS_SERVICE_PORT', 5001))
    app.run(port=port, debug=True)
