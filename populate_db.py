from shared.utils.db_utils import db
from shared.models.user_model import User
from shared.models.post_model import Post
from flask import Flask
import random
from werkzeug.security import generate_password_hash
from datetime import datetime
# Initialize the Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/social_media_app_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create the database tables
with app.app_context():
    db.create_all()  # Create all tables

    # Dummy users
    

    users = [
        User(username='user1', email='user1@example.com', 
            password_hash=generate_password_hash('password1'), created_at=datetime.utcnow()),
        User(username='user2', email='user2@example.com', 
            password_hash=generate_password_hash('password2'), created_at=datetime.utcnow()),
        User(username='user3', email='user3@example.com', 
            password_hash=generate_password_hash('password3'), created_at=datetime.utcnow()),
        User(username='user4', email='user4@example.com', 
            password_hash=generate_password_hash('password4'), created_at=datetime.utcnow()),
        User(username='user5', email='user5@example.com', 
            password_hash=generate_password_hash('password5'), created_at=datetime.utcnow())
    ]


    # Add users to the session
    db.session.bulk_save_objects(users)
    db.session.commit()

    # Create some posts
    posts = [
        Post(user_id=1, content='Post from user1'),
        Post(user_id=2, content='Post from user2'),
        Post(user_id=3, content='Post from user3'),
        Post(user_id=4, content='Post from user4'),
        Post(user_id=5, content='Post from user5'),
        Post(user_id=random.choice([1, 2, 3, 4, 5]), content='Another post from a random user'),
    ]

    # Add posts to the session
    db.session.bulk_save_objects(posts)
    db.session.commit()

    print('Dummy data populated successfully!')
