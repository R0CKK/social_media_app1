from shared.utils.db_utils import db  # Assuming your db instance is defined in db_utils.py
from .user_model import User
from .post_model import Post
from .notification_model import Notification

__all__ = ['db', 'User', 'Post', 'Notification']