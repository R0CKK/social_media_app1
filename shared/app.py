from flask import Flask, session, jsonify, abort, request
from utils.db_utils import db
from utils.db_utils import migrate
from root_services.explore_service import ExploreService
from models.user_model import User  # Ensure User model is imported
import sys, os
sys.path.append(os.getcwd())

# Initialize the Flask App
app = Flask(__name__)

# Initialization configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/social_media_app_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Set your secret key for session management

explore_service = ExploreService()

# User authentication function
def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()  # Fetch user by username
    if user and user.check_password(password):  # Assuming you have a method to check passwords
        return user.id  
    return None  

# Route for user login
@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists'}), 400

    new_user = User(username=username)
    new_user.set_password(password)  # Hash and set the password
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    user_id = authenticate_user(username, password)  # Authenticate user
    if user_id:
        session['user_id'] = user_id  
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None) 
    return jsonify({'message': 'Logout successful'}), 200

@app.route('/explore', methods=['GET'])
def explore():
    current_user_id = session.get('user_id')
    if current_user_id is None:
        abort(401, description="Unauthorized access. Please log in.")

    trending_posts = explore_service.get_trending_posts()
    suggested_users = explore_service.get_suggested_users(current_user_id)

    return jsonify({
        'trending_posts': [post.to_dict() for post in trending_posts],
        'suggested_users': [user.to_dict() for user in suggested_users]
    })

db.init_app(app)
migrate.init_app(app, db)
if __name__ == '__main__':
    app.run(debug=True, port=5000)

from shared.models import user_model
from shared.models import post_model
