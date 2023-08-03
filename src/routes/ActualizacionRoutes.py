from flask import Blueprint, jsonify, request
# Entities
from models.entities.Operacion import Operacion
# Import Models
from models.OperacionModel import OperacionModel
from models.OrganizacionModel import OrganizacionModel
# Validates
from models.validates.Validate import Validate
# validate
from utils.FunctionJWT import validate_token
# Enums
from enums.FieldsName import FieldsName
from models.ConsumoServicioSOAP import ConsumoServicioSOAP
from utils import FuncionessUrl
from utils.helpers import obtener_valores_respuesta_soap

from config import Config

main=Blueprint('routes_actualizacion',__name__)

@main.before_request
def verificar_token_middleware():
    try:
        token = request.headers['Authorization'].split(" ")[1]
        validate_token(token)
    except Exception as ex:
        return jsonify({
            "error_code": 403,
            "message": "No tiene autorización para usar el recurso.",
            "error": str(ex)}), 403


@main.route('/estado', methods=['POST'])
def actualizacion():
    operacion=None
    try:
        dominio = Config.DOMINIO
        subdominio = FuncionessUrl.obtener_subdominio(request.url, dominio)
        if(subdominio == None):
            return jsonify({
                "error": "HTTP_AUTHORIZATION",
                "error_code": 403,
                "msg": "[403] No tiene autorización para usar el recurso."
            }), 403
        # Obtener el puerto de la petición
        # port = FuncionessUrl.obtener_puerto_peticion(request.url)
        history_response = request.json
        # Validar la estructura de la peticion desde Anddes
        if Validate.validateRequest(request.json):
            #Obtener id de la organizacion por el puerto de la peticion
            # organizacion_id = OrganizacionModel.obtener_organizacion_id_por_puerto(port)
            #Obtener id de la organizacion por el subdominio de la peticion
            organizacion = OrganizacionModel.obtener_organizacion_id_por_subdominio(subdominio)
            if organizacion == None:
                return jsonify({
                    "ok": False,
                    "msg": "[404] No existe el Email que estas buscando8!",
                    "hystory": history_response
                }), 404
            idmensaje = request.json['idmensaje']
            # Validar si existe el correo en la tabla operacion            
            operacion=OperacionModel.obtener_email_por_idmensaje_y_organizacion_id(idmensaje, organizacion['id'])
            # Si no se encuentra el email se reponde un mensaje de error 400
            if operacion == None:
                # Si No existe el email se reponde un mensaje con codigo 400
                return jsonify({
                    "ok": False,
                    "msg": "[404] No existe el Email que estas buscando!",
                    "hystory": history_response
                }), 404
            
            print(organizacion)
            print(operacion)
            
            # TODO llamar al funcion que lanza el llamdado Andes los datos del email estan operacion
            # response_soap = ConsumoServicioSOAP.soapObtenerToken(
            #     config('DOMINIO_PROVEEDOR'),
            #     organizacion['org_subdominio'], 
            #     organizacion['org_usuariosubdominio'], 
            #     organizacion['org_clave'],
            #     idmensaje,
            #     True
            # )

            #obtener_valores_respuesta_soap(response_soap)

            # TODO enviar correo electronico a 
           

            # Si existe el email se reponde un mensaje con codgio 200
            return jsonify({
                "ok": True,
                "msg": "[200] Se creo Correctamente!",
                "hystory": history_response
            }), 200
        else:
            # Sino se cumple con la estructura desde Anddes se retorna error 500
            history_response[FieldsName.ESTADO.value] = 1 
            return jsonify({
                "ok": False,
                "msg": "[500] Se ha presentado un error inesperado!",
                "hystory": history_response
            }), 500
    except Exception as ex:
        return jsonify({
            "ok": False,
            "msg": "[500] Se ha presentado un error inesperado!",
            "hystory": history_response
            # "error": str(ex)
        }), 500
    
    
    
        

