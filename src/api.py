from flask import Flask
from flask_cors import CORS

from config import config

# Importar Routes
from routes import ActualizacionRoutes
from routes import OperacionRoutes
from routes import OrganizacionRoutes
from routes import UserRoutes
from routes import HandleErrors

app = Flask(__name__)

CORS(app,resources={"*":{"origins":"*"}})

@app.route('/')
def index():
    return "<h1 style='color: blue;'>4-72</h1>",200


app.config.from_object(config['production'])

# Blueprints
app.register_blueprint(ActualizacionRoutes.main, url_prefix='/api/actualizacion')
# app.register_blueprint(OperacionRoutes.main, url_prefix='/api/operaciones')
# app.register_blueprint(OrganizacionRoutes.main, url_prefix='/api/organizaciones')
app.register_blueprint(UserRoutes.main, url_prefix='/api')

# Manejar errores
app.register_error_handler(404, HandleErrors.page_not_found)

if __name__ == '__main__':
    app.run() 
