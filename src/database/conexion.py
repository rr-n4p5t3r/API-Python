import psycopg2
from psycopg2 import DatabaseError
from decouple import config
import pymysql

def conectar():
    try:
        return psycopg2.connect(
            host=config('DB_HOST'),
            user=config('DB_USER'),
            password=config('DB_PASSWORD'),
            database=config('DB_DATABASE')
        )
    except DatabaseError as ex:
        raise ex

def conectar_maria_db():
    try:
        return pymysql.connect(
            host=config('MARIADB_HOST'),
            user=config('MARIADB_USER'),
            password=config('MARIADB_PASSWORD'),
            database=config('MARIADB_DATABASE')
        ) 
    except Exception as ex:
        raise ex