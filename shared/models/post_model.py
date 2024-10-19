from datetime import datetime
from shared.utils.db_utils import db

class Post(db.Model):
    __tablename__ = 'posts'

    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    likes = db.relationship('Like', backref='post', lazy=True)  # Add relationship
    comments_count = db.Column(db.Integer, default=0)
    trending_score = db.Column(db.Integer, default=0)  # New field
    notifications = db.relationship('Notification', back_populates='post',lazy = 'dynamic')
    from shared.models.notification_model import Notification
    user = db.relationship('User', viewonly=True)  # Read-only relationship
    author = db.relationship('User')
class Like(db.Model):
    __tablename__ = 'likes'

    like_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
class Comment(db.Model):
    __tablename__ = 'comments'

    comment_id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)