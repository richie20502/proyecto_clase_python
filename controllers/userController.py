from models.User import User
from flask import jsonify
from config import db

def get_all_users():
    try:
        return [ user.to_dict() for user in User.query.all()]    
    except Exception as error:
        print(f"ERROR {error}")
        
        #return jsonify(error)

def create_user(name, email):
    try:
        new_user = User(name, email)
    
        db.session.add(new_user)
        db.session.commit()
        
        return new_user.to_dict()

    except Exception as e:
        print(f"ERROR {e}")
    