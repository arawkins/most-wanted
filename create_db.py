from config import SQLALCHEMY_DATABASE_URI
from main import db

db.create_all()
