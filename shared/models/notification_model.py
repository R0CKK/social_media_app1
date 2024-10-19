from datetime import datetime
from sqlalchemy import  Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from shared.utils.db_utils import db
class Notification(db.Model):
    __tablename__ = 'notifications'

    id = db.Column(Integer, primary_key=True)
    user_id = db.Column(Integer, ForeignKey('users.user_id'))  # The user receiving the notification
    message = db.Column(String(255), nullable=False)
    read = db.Column(Boolean, default=False)  # To track whether the notification has been read
    timestamp = db.Column(DateTime, default=datetime.utcnow)
    post_id = db.Column(Integer, ForeignKey('posts.post_id'), nullable=True)  # If related to a post
    comment_id = db.Column(Integer, ForeignKey('comments.comment_id'), nullable=True)  # If related to a comment

    # Relationships
    user = db.relationship("User", back_populates="notifications")
    post = db.relationship("Post", back_populates="notifications")