from flask import Blueprint, jsonify, request
# Import Models
from models.OrganizacionModel import OrganizacionModel
#
from utils.FunctionJWT import validate_token

main=Blueprint('routes_organizacion',__name__)

@main.before_request
def verificar_token_middleware():
    token = request.headers['Authorization'].split(" ")[1]
    validate_token(token, output=False)

@main.route('/')
def get_organizaciones():
    try:
        organizaciones = OrganizacionModel.obtener_organizaciones()
        return jsonify(organizaciones)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

@main.route('/puertos')
def get_puertos():
    try:
        organizaciones = OrganizacionModel.obtener_puerto_organizacion()
        return jsonify(organizaciones)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
