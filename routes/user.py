from flask import Blueprint, jsonify, request
from controllers.userController import get_all_users, create_user

user_bp = Blueprint('users', __name__)
@user_bp.route('/', methods=['GET'])
def index():
    """
    Obtener todos los usuarios
    ---
    tags:
      - Usuarios
    responses:
      200:
        description: Lista de usuarios
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              name:
                type: string
                example: "Juan Pérez"
              email:
                type: string
                example: "juan@example.com"
    """
    user = get_all_users()
    return jsonify(user)

@user_bp.route('/', methods = ['POST'])
def user_store():
    """
    Crear un usuario
    ---
    tags:
      - Usuarios
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - name
            - email
          properties:
            name:
              type: string
              example: "Juan Pérez"
            email:
              type: string
              example: "juan@example.com"
    responses:
      201:
        description: Usuario creado
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            name:
              type: string
              example: "Juan Pérez"
            email:
              type: string
              example: "juan@example.com"
      400:
        description: Error en los datos enviados
    """
    data = request.get_json()
    email = data.get('email') 
    name = data.get('name')
    print(f"NAME {name} --- email {email}")
    new_user = create_user(name, email)
    return jsonify(new_user)
