from shared.utils.db_utils import Session
from shared.models.notification_model import Notification
from shared.models.user_model import User
from shared.models.post_model import Post,Comment,Like


class NotificationManager:
    def __init__(self):
        self.session = Session()

    def notify_followers(self, post: Post):
        # Notify all followers of the post's author about the new post
        followers = post.author.followers
        for follower in followers:
            message = f"{post.author.username} has posted something new!"
            self.create_notification(follower.id, message, post_id=post.id)

    def notify_post_owner_on_comment(self, comment: Comment):
        # Notify the owner of the post when someone comments on their post
        post_owner = comment.post.author
        message = f"{comment.author.username} commented on your post."
        self.create_notification(post_owner.id, message, post_id=comment.post.id, comment_id=comment.id)

    def notify_post_owner_on_like(self, post: Post, liker: User):
        # Notify the owner of the post when someone likes their post
        post_owner = post.author
        message = f"{liker.username} liked your post."
        self.create_notification(post_owner.id, message, post_id=post.id)

    def create_notification(self, user_id: int, message: str, post_id=None, comment_id=None):
        notification = Notification(
            user_id=user_id,
            message=message,
            post_id=post_id,
            comment_id=comment_id
        )
        self.session.add(notification)
        self.session.commit()

    def get_unread_notifications(self, user_id: int):
        notifications = self.session.query(Notification).filter_by(user_id=user_id, read=False).all()
        return notifications

    def mark_as_read(self, notification_id: int):
        notification = self.session.query(Notification).get(notification_id)
        if notification:
            notification.read = True
            self.session.commit()
