from flask import Flask, jsonify, request 
from dotenv import load_dotenv 
import os 
# Cargar variables de entorno 
load_dotenv() 
app = Flask(__name__) 
# Simulación de base de datos 
usuarios = [ 
    {"id": 1, "nombre": "Ana", "email": "ana@ejemplo.com"}, 
    {"id": 2, "nombre": "Berto", "email": "berto@ejemplo.com"} 
] 
 
@app.route('/api/usuarios', methods=['GET']) 
def obtener_usuarios(): 
    return jsonify({ 
        "servicio": "usuarios", 
        "data": usuarios, 
        "status": "success" 
    }) 
 
@app.route('/api/usuarios/<int:usuario_id>', methods=['GET']) 
def obtener_usuario(usuario_id): 
    usuario = next((u for u in usuarios if u['id'] == usuario_id), None) 
    if usuario: 
        return jsonify({ 
            "servicio": "usuarios", 
            "data": usuario, 
            "status": "success" 
        }) 
    return jsonify({"error": "Usuario no encontrado", "status": "error"}), 404 
 
@app.route('/api/usuarios/healthcheck', methods=['GET']) 
def healthcheck(): 
    return jsonify({"status": "healthy", "service": "usuarios"}) 
 
if __name__ == '__main__': 
    port = int(os.getenv('USERS_SERVICE_PORT', 5000)) 
    
app.run(port=port, debug=True)