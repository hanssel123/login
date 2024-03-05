from flask import Flask, request, jsonify
from flask_cors import CORS
import jwt
import datetime

app = Flask(__name__)
CORS(app, supports_credentials=True, origins=["http://localhost:3000"])

# Clave secreta para firmar el token
SECRET_KEY = 'tu_clave_secreta'

# Lista para almacenar todos los mensajes (enviados y recibidos)
all_messages = []

@app.route('/auth', methods=['POST'])
def authenticate():
    data = request.get_json()
    user = data.get('user', '')
    pwd = data.get('pwd', '')
    if pwd == "123":
        # Crear token JWT con el rol de administrador
        token_payload = {'user': user, 'role': 'admin', 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}
        token = jwt.encode(token_payload, SECRET_KEY)
        return jsonify({'role':'admin','token':token}), 200
    else:
        return jsonify({'error': 'Credenciales invalidas'}), 401

if __name__ == '__main__':
    app.run(debug=True)
