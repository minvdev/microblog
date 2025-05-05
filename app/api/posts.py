from app.api import bp
from app.api.auth import token_auth
from app import db
from app.models import Post
import sqlalchemy as sa
from flask import request, url_for, abort
from app.api.errors import bad_request
from langdetect import detect, LangDetectException

@bp.route('/posts/<int:id>', methods=['GET'])
@token_auth.login_required
def get_post(id):
    """Return a post from an id"""
    return db.get_or_404(Post, id).to_dict()

@bp.route('/posts', methods=['GET'])
@token_auth.login_required
def get_posts():
    """Return all posts from the db"""
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    return Post.to_collection_dict(sa.select(Post), page, per_page,
                                   'api.get_posts')

@bp.route('/posts', methods=['POST'])
@token_auth.login_required
def create_post():
    """Share a new post"""
    data = request.get_json()
    if 'body' not in data:
        return bad_request('Must include body field')
    
    if len(data['body']) > 140:
        return bad_request('Body cannot exceed 140 characters')
    
    data['user_id'] = token_auth.current_user.id if token_auth.current_user.id \
        else bad_request('The user id could not be found')
    
    try:
        data['language'] = detect(data['body'])
    except LangDetectException:
        data['language'] = ''
    
    post = Post()
    post.from_dict(data)
    db.session.add(post)
    db.session.commit()
    return post.to_dict(), 201, {'Location': url_for('api.get_post',
                                                     id=post.id)}
