from app.api import bp
from app import db
from app.models import User

@bp.route('/users/<int:id>', methods=['GET'])
# Return a user
def get_user(id):
    return db.get_or_404(User, id).to_dict()

@bp.route('/users', methods=['GET'])
# Return the collection of all users
def get_users():
    pass

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
