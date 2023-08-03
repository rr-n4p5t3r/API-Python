from flask import Blueprint, request, jsonify, json
from utils.FunctionJWT import write_token_without_expiration_date, validate_token
# Import Models
from models.UserModel import UserModel
# Entities
from models.entities.User import User

main=Blueprint('routes_user',__name__)

@main.route('obtenerToken', methods=['POST'])
def login():
    try:
        # Obtener Usuario y Password de la peticion
        username = request.json['username']
        password = request.json['password']
        # Obtener informacion del usuario en la BD
        user_payload = User(0, username, password)
        user_logged = UserModel.login(user_payload)
        # Varificar si el usuario existe en la BD y verificar password
        if user_logged != None and user_logged.password:
            token = write_token_without_expiration_date(user_payload.to_JSON())
            # return token.decode('UTF-8')
            return jsonify({
                "message": "Obtención de token exitoso!",
                "username": username,
                "token": token.decode('UTF-8')
            })
        else:
            return jsonify({
                "error_code": 401,
                "message": "Credenciales no válidas!"
            }), 401
    except Exception as ex:
        return jsonify({
            "success": False,
            "error_code": 500,
            "message": "Ha ocurrido un error en el servidor.",
            "error": str(ex)
        }), 500
@main.route("verificarToken")
def verify():
    token = request.headers['Authorization'].split(" ")[1]
    return validate_token(token, output=True)