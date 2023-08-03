from jwt import decode, encode
from jwt import exceptions
from decouple import config
from datetime import datetime, timedelta
from flask import jsonify

#print(config('SECRET_KEY'))

def expire_date(days: int):
    now = datetime.now()
    new_date = now + timedelta(days)
    return new_date

def write_token(data: dict):
    token = encode(payload={
                    **data, 
                    "exp": expire_date(int(config('DAYS_EXP')))
                }, 
                key=config('SECRET_KEY'), 
                algorithm="HS256")
    return token.encode("UTF-8")

def write_token_without_expiration_date(data: dict):
    token = encode(payload={**data}, 
                   key=config('SECRET_KEY'), 
                   algorithm="HS256")
    return token.encode("UTF-8")

def validate_token(token, output=False):
    try:
        if output:
            user = decode(token, key=config('SECRET_KEY'), algorithms=["HS256"])
            user.pop('id')
            user.pop('password')
            user['message']="Token Válido"
            return user
        decode(token, key=config('SECRET_KEY'), algorithms=["HS256"])
    except exceptions.DecodeError:
        response = jsonify({"message": "Token Inválidos"})
        response.status_code = 401
        return response
    except exceptions.ExpiredSignatureError:
        response = jsonify({"message": "Token Expirado"})
        response.status_code = 401
        return response