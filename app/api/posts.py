from app.api import bp
from app.api.auth import token_auth

@bp.route('/posts/<id>', methods=['GET'])
@token_auth.login_required
def get_post(id):
    """Return a post from an id"""

@bp.route('/posts', methods=['GET'])
@token_auth.login_required
def get_posts():
    """Return all posts from the db"""

@bp.route('/posts', methods=['POST'])
@token_auth.login_required
def create_post():
    """Share a new post"""
