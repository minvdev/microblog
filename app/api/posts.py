from app.api import bp
from app.api.auth import token_auth
from app import db
from app.models import Post
import sqlalchemy as sa
from flask import request

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
