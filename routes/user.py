from flask import Blueprint, jsonify, request
from controllers.userController import get_all_users, create_user, login_user
from flask_jwt_extended import jwt_required, get_jwt_identity

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
    """
    users = get_all_users()
    return jsonify(users)

@user_bp.route('/', methods=['POST'])
def user_store():
    """
    Crear un usuarios
    ---
    tags:
      - Usuarios
    parameters:
      - in: body
        name: user
        schema:
          type: object
          required:
            - name
            - email
            - password
          properties:
            name:
              type: string
              example: "Juan Pérez"
            email:
              type: string
              example: "juan@example.com"
            password:
              type: string
              example: "123456"
    responses:
      201:
        description: Usuario creado
    """
    data = request.get_json()
    user = create_user(data['name'], data['email'], data['password'])
    return jsonify(user), 201

@user_bp.route('/login', methods=['POST'])
def login():
    """
    Iniciar sesión
    ---
    tags:
      - Autenticación
    parameters:
      - in: body
        name: credentials
        schema:
          type: object
          required:
            - email
            - password
          properties:
            email:
              type: string
              example: "juan@example.com"
            password:
              type: string
              example: "123456"
    responses:
      200:
        description: Login exitoso
    """
    data = request.get_json()
    return login_user(data['email'], data['password'])

@user_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    """
    Obtener perfil del usuario autenticado
    ---
    tags:
      - Usuarios
    responses:
      200:
        description: Datos del usuario
    """
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return jsonify({"msg": "Usuario no encontrado"}), 404

    return jsonify(user.to_dict())
