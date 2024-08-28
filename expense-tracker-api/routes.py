import os
import jwt
from flask import Blueprint, request, jsonify
from datetime import datetime, timedelta
from models import db, bcrypt, User, Expense


bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully!'})

