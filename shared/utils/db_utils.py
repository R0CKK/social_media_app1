from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
db = SQLAlchemy()

migrate = Migrate()
DATABASE_URL = 'mysql+pymysql://root:password@localhost/social_media_app_db'

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
def init_app(app):
    db.init_app(app)
    migrate.init_app(app, db)