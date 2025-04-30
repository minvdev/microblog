from app.api import bp
from app import db
from app.models import User
import sqlalchemy as sa
from flask import request

@bp.route('/users/<int:id>', methods=['GET'])
# Return a user
def get_user(id):
    return db.get_or_404(User, id).to_dict()

@bp.route('/users', methods=['GET'])
# Return the collection of all users
def get_users():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    return User.to_collection_dict(sa.select(User), page, per_page,
                                   'api.get_users')

@bp.route('/users/<int:id>/followers', methods=['GET'])
# Return the followers of this user
def get_followers(id):
    pass

@bp.route('/users/<int:id>/following', methods=['GET'])
# Return the users this user is following
def get_following(id):
    pass

@bp.route('/users', methods=['POST'])
# Register a new user account
def create_user():
    pass

@bp.route('/users/<int:id>', methods=['PUT'])
# Modify a user
def update_user(id):
    pass
