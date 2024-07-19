from config import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.sql import func

class User(db.Model, SerializerMixin):
  __tabelename__ = 'users'
  
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String, nullable = False, unique = True)
  email = db.Column(db.String, nullable = False, unique = True)
  mobile_number = db.Column(db.Integer, nullable = False, unique = True)
  
# class Post(db.Model, SerializerMixin):
#   __tabelename__ = 'posts'
  
#   id = db.Column(db.Integer, primary_key=True)
#   title = db.Column(db.String, nullable = False, unique = True)
#   body = db.Column(db.String)
#   created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
#   updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
#   user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  
# class Category(db.Model, SerializerMixin):
#   __tabelename__ = 'categories'
  
#   id = db.Column(db.Integer, primary_key=True)
#   title = db.Column(db.String, nullable = False, unique = True)