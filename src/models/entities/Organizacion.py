from utils.DateFormat import DateFormat
class Organizacion():

    def __init__(self,org_id,org_nombre=None,org_puerto=None,org_creado=None,org_actualizado=None,org_dominiodeemicion=None,org_subdominio=None,org_usuariosubdominio=None,org_clave=None,org_estado=None,org_nit=None) -> None:
        self.org_id=org_id
        self.org_nombre=org_nombre
        self.org_dominiodeemicion=org_dominiodeemicion
        self.org_subdominio=org_subdominio
        self.org_usuariosubdominio=org_usuariosubdominio
        self.org_clave=org_clave
        self.org_creado=org_creado
        self.org_actualizado=org_actualizado
        self.org_estado=org_estado
        self.org_nit=org_nit
        self.org_puerto=org_puerto

    def to_JSON(self):
        return {
            'id': self.org_id,
            'nombre': self.org_nombre,
            'puerto': self.org_puerto,
            'creado': DateFormat.convert_date(self.org_creado) if self.org_creado is not None else self.org_creado,
            'actualizado': DateFormat.convert_date(self.org_actualizado) if self.org_actualizado is not None else self.org_actualizado,
            'dominio_de_emicion': self.org_dominiodeemicion,
            'subdominio': self.org_subdominio,
            'usuario_subdominio': self.org_usuariosubdominio,
            'clave': self.org_clave,            
            'estado': self.org_estado,
            'nit': self.org_nit
        }
    

    def ports_To_JSON(self):
        return {
            'id': self.org_id,
            'nombre': self.org_nombre,
            'puerto': self.org_puerto
        }