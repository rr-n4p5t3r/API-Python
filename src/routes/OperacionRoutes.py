from flask import Blueprint, jsonify, request
# Import Models
from models.OperacionModel import OperacionModel
#
from utils.FunctionJWT import validate_token

main=Blueprint('routes_operacion',__name__)


@main.before_request
def verificar_token_middleware():
    token = request.headers['Authorization'].split(" ")[1]
    validate_token(token, output=False)

@main.route('/')
def get_operaciones():
    try:
        operaciones = OperacionModel.obtener_operaciones()
        return jsonify(operaciones)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500