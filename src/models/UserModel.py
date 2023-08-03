from database.conexion import conectar_maria_db
from .entities.User import User
class UserModel():
    @classmethod
    def login(self, user):
        try:
            connection=conectar_maria_db()
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, username, password FROM users WHERE username = %s", [user.username])
                row=cursor.fetchone()
                user_db=None
                if row !=  None:
                    password = User.check_password(row[2], user.password);
                    user_db = User( row[0], row[1], password)
                    # user_db = user_db.to_JSON()
            connection.close()
            return user_db
        except Exception as ex:
            raise Exception(ex)