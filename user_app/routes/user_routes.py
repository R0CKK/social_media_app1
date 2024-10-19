from flask import Blueprint
from user_app.controllers.user_controller import UserController


user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/api/users', methods=['GET'])
def get_all_users():
    print("ss")
    return UserController.get_all_users()

@user_bp.route('/api/users/<username>', methods=['GET'])
def get_user(username):
    return UserController.get_user(username)

@user_bp.route('/api/users', methods=['POST'])
def create_user():
    return UserController.create_user()

@user_bp.route('/api/users/login', methods=['POST'])
def login_user():
    return UserController.login_user()
@user_bp.route('/api/users/follow', methods=['POST'])
def follow_user():
    return UserController.follow_user()

@user_bp.route('/api/users/unfollow', methods=['POST'])
def unfollow_user():
    return UserController.unfollow_user()

@user_bp.route('/api/users/<username>/followers', methods=['GET'])
def get_followers(username):
    return UserController.get_followers(username)

@user_bp.route('/api/users/<username>/following', methods=['GET'])
def get_following(username):
    return UserController.get_following(username)
