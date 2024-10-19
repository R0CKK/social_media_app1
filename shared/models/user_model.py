from datetime import datetime
from shared.utils.db_utils import db
from werkzeug.security import generate_password_hash, check_password_hash
class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    def set_password(self, password):
        """Hash the password and store it."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check if the provided password matches the stored password hash."""
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        """Convert user model to dictionary for API response."""
        return {
            'id': self.id,
            'username': self.username,
            # Include other fields as necessary
        }
    full_name = db.Column(db.String(255))
    bio = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    notifications = db.relationship('Notification', back_populates='user',lazy = 'dynamic')
    posts = db.relationship('Post', back_populates='author',lazy = 'dynamic')
    from shared.models.notification_model import Notification
    # Relationships for followers and following
    followers = db.relationship('Follow', foreign_keys='Follow.followed_id', backref='followed', lazy='dynamic')
    following = db.relationship('Follow', foreign_keys='Follow.follower_id', backref='follower', lazy='dynamic')
class Follow(db.Model):
    __tablename__ = 'follows'

    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    followed_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
