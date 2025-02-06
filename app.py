from flask import Flask
from config import db, migrate
from dotenv import load_dotenv
from flask_cors import CORS
from flasgger import Swagger
import os

# Cargar variables de entorno
load_dotenv()

# Crear instancia de Flask
app = Flask(__name__)
CORS(app)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SWAGGER'] = {
    'title': 'Mi API Flask',
    'uiversion': 3
}

# Inicializar extensiones
db.init_app(app)
migrate.init_app(app, db)

swagger = Swagger(app)

# Registrar rutas
from routes.user import user_bp
app.register_blueprint(user_bp, url_prefix='/users')

if __name__ == '__main__':
    app.run(debug=True)
