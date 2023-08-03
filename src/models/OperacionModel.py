from database.conexion import conectar
from .entities.Operacion import Operacion

class OperacionModel():

    @classmethod
    def obtener_operaciones(self):
        try:
            connection=conectar()
            operaciones=[]

            with connection.cursor() as cursor:
                cursor.execute("""SELECT opr_id, fopr_id, opr_idientificadoranddes, opr_idientificadorcliente, opr_correoemisor, opr_creado, opr_actualizado,opr_estado,opr_asunto,opr_correoorganizacion,opr_destinatario 
                    FROM operacion 
                    ORDER BY opr_id DESC 
                    LIMIT 10""")
                resultset=cursor.fetchall()

                for row in resultset:
                    operacion=Operacion(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])
                    operaciones.append(operacion.to_JSON())

            connection.close()
            return operaciones
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def obtener_email_por_idmensaje_y_organizacion_id(self, idmensaje, organizacion_id):
        try:
            connection=conectar()
            with connection.cursor() as cursor:
                cursor.execute("""SELECT opr_id, fopr_id, opr_idientificadoranddes, opr_idientificadorcliente, opr_correoemisor, opr_creado, opr_actualizado,opr_estado,opr_asunto,opr_correoorganizacion,opr_destinatario
                    FROM operacion 
                    WHERE opr_Idientificadoranddes=%s
                    AND fopr_id=%s""", (idmensaje, organizacion_id))
                row=cursor.fetchone()
                operacion=None
                if row !=  None:
                    operacion=Operacion(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])
                    operacion=operacion.to_JSON()

            connection.close()
            return operacion                
        except Exception as ex:
            raise Exception(ex)

