import xml.etree.ElementTree as ET
from werkzeug.security import generate_password_hash
from urllib.parse import urlparse
import secrets
from flask import jsonify

def obtener_valores_respuesta_soap(soap_response):
    # Parsear el XML
    root = ET.fromstring(soap_response)

    # Obtener el elemento "hash" dentro de "ObtenerTokenResponse"
    hash_element = root.find('.//ns1:ObtenerTokenResponse/ns1:hash', namespaces={'ns1': 'http://www.sealmail.co/'})

    # Obtener los valores de "IdMensaje", "Token" y "Observacion"
    hash_string = hash_element.text
    id_mensaje = None
    token = None
    observacion = None

    for item in hash_string.split('|'):
        key, value = item.split('=')
        if key == 'IdMensaje':
            id_mensaje = value
        elif key == 'Token':
            token = value
        elif key == 'Observacion':
            observacion = value

    # return los valores obtenidos
    return id_mensaje, token, observacion

def generar_password(username,password):
    password = generate_password_hash(password)
    print(f"username: {username}")
    print(end=f"Hashed password: {password}")
    print(end=" ")

def obtener_puerto_peticion(url):
    parts_url = urlparse(url)
    return parts_url.port

def obtener_subdominio(url, dominio):
    parts_url = urlparse(url)
    host = parts_url.hostname    
    # Verificar si el dominio actual es igual al dominio válido
    if host == dominio:
        return None  # No hay subdominio
    else:
        # Obtener la parte final del dominio
        dominio_actual = '.'.join(host.split('.')[-2:])
        # Obtener el subdominio
        subdominio = host[:-(len(dominio_actual) + 1)]
        return subdominio

def generar_secreto_256_bits():
    return secrets.token_hex(32)