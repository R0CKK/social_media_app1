from flask import request
from user_app.services.user_service import UserService
from user_app.views.user_view import UserView


class UserController:
    @staticmethod
    def get_all_users():
        users = UserService.get_all_users()
        return UserView.render_users(users), 200

    @staticmethod
    def get_user(username):
        user = UserService.get_user_by_username(username)
        if not user: # if user is None:
            return UserView.render_error('User not found'), 404
        return UserView.render_user(user), 200

    @staticmethod
    def create_user():
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        full_name = data.get('full_name', '')
        bio = data.get('bio', '')

        user = UserService.create_user(username, email, password, full_name, bio)
        return UserView.render_success('User created successfully', user.user_id), 201

    @staticmethod
    def login_user():
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user = UserService.verify_user(username, password)
        if user:
            return UserView.render_success('Login successful', user.user_id), 200
        return UserView.render_error('Invalid username or password'), 401
    @staticmethod
    def follow_user():
        data = request.get_json()
        follower_id = data.get('follower_id')
        followed_id = data.get('followed_id')
        follow = UserService.follow_user(follower_id, followed_id)
        if follow:
            return UserView.render_success('User followed successfully'), 201
        return UserView.render_error('Already following or invalid request'), 409

    @staticmethod
    def unfollow_user():
        data = request.get_json()
        follower_id = data.get('follower_id')
        followed_id = data.get('followed_id')
        unfollow = UserService.unfollow_user(follower_id, followed_id)
        if unfollow:
            return UserView.render_success('User unfollowed successfully'), 200
        return UserView.render_error('Not following the user'), 404

    @staticmethod
    def get_followers(username):
        user = UserService.get_user_by_username(username)
        if not user:
            return UserView.render_error('User not found'), 404
        followers = UserService.get_followers(user.user_id)
        return UserView.render_followers(followers), 200

    @staticmethod
    def get_following(username):
        user = UserService.get_user_by_username(username)
        if not user:
            return UserView.render_error('User not found'), 404
        following = UserService.get_following(user.user_id)
        return UserView.render_following(following), 200