from shared.models.post_model import Post
from shared.models.user_model import User
from shared.utils.db_utils import session


class ExploreService:
    @staticmethod
    def get_trending_posts():
        return session.query(Post).order_by(Post.trending_score.desc()).limit(10).all()

    @staticmethod
    def get_suggested_users(current_user_id):
        # Simple example: suggest users not followed by the current user
        followed_user_ids = session.query(User.following).filter(User.id == current_user_id).first()
        return session.query(User).filter(User.id.notin_(followed_user_ids)).limit(5).all()
