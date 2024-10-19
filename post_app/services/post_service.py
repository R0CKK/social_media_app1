from shared.models.post_model import Post,Like,Comment
from shared.utils.db_utils import db
from shared.root_services.notification_manager import NotificationManager

class PostService:
    @staticmethod
    def create_post(user_id, content):
        new_post = Post(user_id=user_id, content=content)
        db.session.add(new_post)
        db.session.commit()
        NotificationManager.notify_followers_of_post(user_id)
        return new_post

    @staticmethod
    def get_post_by_id(post_id):
        return Post.query.filter_by(post_id=post_id).first()

    @staticmethod
    def get_posts_by_user(user_id):
        return Post.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_all_posts():
        return Post.query.order_by(Post.created_at.desc()).all()

    @staticmethod
    def update_post(post_id, new_content):
        post = Post.query.filter_by(post_id=post_id).first()
        if post:
            post.content = new_content
            db.session.commit()
        return post

    @staticmethod
    def delete_post(post_id):
        post = Post.query.filter_by(post_id=post_id).first()
        if post:
            db.session.delete(post)
            db.session.commit()
        return post
    @staticmethod
    def like_post(post_id, user_id):
        like = Like.query.filter_by(post_id=post_id, user_id=user_id).first()
        if not like:
            new_like = Like(user_id=user_id, post_id=post_id)
            db.session.add(new_like)
            db.session.commit()
            post_author_id = db.session.query(Post).filter_by(id=post_id).first().user_id
            NotificationManager.notify_on_like(user_id, post_author_id)
            
            return new_like
        return None  # User already liked the post
    @staticmethod
    def add_comment(post_id, user_id, content):
        new_comment = Comment(post_id=post_id, user_id=user_id, content=content)
        db.session.add(new_comment)
        db.session.commit()
        NotificationManager.notify_on_comment(user_id, post_id)
        return new_comment
    @staticmethod
    def share_post(post_id, user_id):
        # Simulate sharing by copying the post to the user's account
        post = Post.query.get(post_id)
        if post:
            shared_post = Post(user_id=user_id, content=f"Shared: {post.content}")
            db.session.add(shared_post)
            db.session.commit()
            return shared_post
        return None