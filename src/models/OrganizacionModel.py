from database.conexion import conectar
from .entities.Organizacion import Organizacion

class OrganizacionModel():

    @classmethod
    def obtener_organizaciones(self):
        try:
            connection=conectar()
            organizaciones=[]
            with connection.cursor() as cursor:
                cursor.execute("""SELECT org_id, org_nombre, org_puerto, org_creado, org_actualizado, org_dominiodeemicion, org_subdominio, org_usuariosubdominio, org_clave, org_estado, org_nit
                                    FROM organizacion 
                                    ORDER BY org_nombre 
                                    LIMIT 10""")
                resultset=cursor.fetchall()

                for row in resultset:
                    print(row)                    
                    organizacion=Organizacion(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])
                    organizaciones.append(organizacion.to_JSON()) 

            connection.close()
            return organizaciones                
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def obtener_puerto_organizacion(self):
        try:
            connection=conectar()
            organizaciones=[]
            with connection.cursor() as cursor:
                cursor.execute("""SELECT org_id, org_nombre, org_puerto, org_creado, org_actualizado 
                                FROM organizacion 
                                WHERE org_puerto IS NOT NULL 
                                ORDER BY org_puerto""")                
                resultset=cursor.fetchall()

                for row in resultset:
                    print(row)
                    organizacion=Organizacion(row[0],row[1],row[2])
                    organizaciones.append(organizacion.ports_To_JSON())
                print(organizaciones)
            connection.close()
            return organizaciones                
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def obtener_organizacion_id_por_puerto(self, puerto):
        try:
            connection=conectar()
            with connection.cursor() as cursor:
                cursor.execute("SELECT org_id FROM organizacion WHERE org_puerto = %s", [puerto])
                row=cursor.fetchone()
                
                organizacion=None
                if row !=  None:
                    organizacion=row[0]

            connection.close()
            return organizacion                
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def obtener_organizacion_id_por_subdominio(self, subdominio):
        try:
            connection=conectar()
            with connection.cursor() as cursor:
                cursor.execute("SELECT org_id, org_subdominio, org_usuariosubdominio, org_clave FROM organizacion WHERE org_subdominio = %s", [subdominio])
                row=cursor.fetchone() 
                organizacion=None               
                if row !=  None:
                    organizacion = {
                        'id' : row[0],
                        'org_subdominio' : row[0],
                        'org_usuariosubdominio' : row[1],
                        'org_clave' : row[2]
                    }                
                return organizacion                    
            connection.close()
            return organizacion    
        except Exception as ex:
            raise Exception(ex)