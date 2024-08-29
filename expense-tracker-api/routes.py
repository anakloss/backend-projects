import os
import jwt
from flask import Blueprint, request, jsonify
from functools import wraps
from datetime import datetime, timedelta
from models import db, bcrypt, User, Expense


bp = Blueprint('api', __name__, url_prefix='/api')


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        
        try:
            jwt_secret_key = os.environ.get('JWT_SECRET_KEY')
            data = jwt.decode(token, jwt_secret_key, algorithms=["HS256"])
            current_user = User.query.filter_by(id=data['user_id']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 403
        return f(current_user, *args, **kwargs)
    
    return decorator

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully!'})

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        token = jwt.encode({'user_id': user.id, 'exp': datetime.utcnow() + timedelta(hours=1)},
                        os.environ.get('JWT_SECRET_KEY'), algorithm='HS256')
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials!'})

@bp.route('/expenses', methods=['GET'])
@token_required
def get_expenses(current_user):
    filters = request.args
    query = Expense.query.filter_by(user_id=current_user.id)
    
    if 'term' in filters:
        term = filters.get('term')
        query = query.filter(Expense.title.ilike(f'%{term}%'))
    
    if 'start_date' in filters and 'end_date' in filters:
        start_date = datetime.strptime(filters.get('start_date'), '%Y-%m-%d')
        end_date = datetime.strptime(filters.get('end_date'), '%Y-%m-%d')
        query = query.filter(Expense.date.between(start_date, end_date))

    expenses = query.all()
    result = [{'id': expense.id, 'title': expense.title, 'amount': expense.amount, 'date': expense.date} for expense in expenses]
    return jsonify(result)

@bp.route('/expenses', methods=['POST'])
@token_required
def add_expense(current_user):
    data = request.get_json()
    new_expense = Expense(title=data['title'], amount=data['amount'], user_id=current_user.id)
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({'message': 'Expense added successfully!'})

@bp.route('/expenses/<int:expense_id>', methods=['PUT'])
@token_required
def update_expense(current_user, expense_id):
    data = request.get_json()
    expense = Expense.query.filter_by(id=expense_id, user_id=current_user.id).first()
    if expense:
        expense.title = data.get('title', expense.title)
        expense.amount = data.get('amount', expense.amount)
        expense.date = datetime.strptime(data.get('date', expense.date.strftime('%Y-%m-%d')), '%Y-%m-%d')
        db.session.commit()
        return jsonify({'message': 'Expense updated successfully!'})
    return jsonify({'message': 'Expense not found!'})
        
@bp.route('/expenses/<int:expense_id>', methods=['DELETE'])
@token_required
def delete_expense(current_user, expense_id):
    expense = Expense.query.filter_by(id=expense_id, user_id=current_user.id).first()
    if expense:
        db.session.delete(expense)
        db.session.commit()
        return jsonify({'message': 'Expense deleted successfully!'})
    return jsonify({'message': 'Expense not found!'})