from flask import Blueprint, request, jsonify
from sqlalchemy import or_
from models import db, Post

bp = Blueprint('posts', __name__, url_prefix='/posts')

@bp.route('/', methods=['POST'])
def create_post():
    data = request.get_json()
    new_post = Post(
        title=data['title'],
        content=data['content'],
        category=data['category'],
        tags=data.get('tags', [])
    )
    db.session.add(new_post)
    db.session.commit()
    return jsonify({'message': 'Post created', 'post': data}), 201

@bp.route('/', methods=['GET'])
def get_posts():
    term = request.args.get('term', None)
    
    if term:
        search =  f"%{term}%"
        posts  = Post.query.filter(
            or_(
                Post.title.ilike(search),
                Post.content.ilike(search),
                Post.category.ilike(search)
            )
        ).all()
    else:
        posts = Post.query.all()
    
    result = [
        {
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'category': post.category,
            'tags': post.tags
        } for post in posts
    ]
    
    return jsonify(result)

@bp.route('/<int:id>', methods=['GET'])
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify({
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'category': post.category,
        'tags': post.tags
    })

@bp.route('/<int:id>', methods=['PUT'])
def update_post(id):
    data = request.get_json()
    post = Post.query.get_or_404(id)
    post.title = data['title']
    post.content = data['content']
    post.category = data['category']
    post.tags = data.get('tags', [])
    db.session.commit()
    return jsonify({'message': 'Post updated', 'post': data})

@bp.route('/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({'message': 'Post deleted'})
