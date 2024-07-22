from config import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.sql import func
from sqlalchemy import Table

class User(db.Model, SerializerMixin):
  __tablename__ = 'users'
  
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String, nullable = False, unique = True)
  email = db.Column(db.String, nullable = False, unique = True)
  mobile_number = db.Column(db.Integer, nullable = False, unique = True)
  
  def __repr__(self):
    return f"""
      id: {self.id}
      username: {self.username}
      email: {self.email}
      mobile_number: {self.mobile_number}
    """
  
class Post(db.Model, SerializerMixin):
  __tablename__ = 'posts'
  
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String, nullable = False, unique = True)
  body = db.Column(db.String)
  created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
  updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  
  def __repr__(self):
    return f"""
      id: {self.id}
      title: {self.title}
      body: {self.body}
      user_id: {self.user_id}
    """
  
class Category(db.Model, SerializerMixin):
  __tablename__ = 'categories'
  
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String, nullable = False, unique = True)
  
  def __repr__(self):
    return f"""
      id: {self.id}
      title: {self.title}
    """
  
  post_category = Table(
    'post_categories',
    db.Model.metadata,
    db.Column('post_id', db.ForeignKey('posts.id'), primary_key=True),
    db.Column('category_id', db.ForeignKey('categories.id'), primary_key=True),
    extend_existing=True,
)