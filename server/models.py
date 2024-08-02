from config import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.sql import func

post_category = db.Table(
  'post_categories',
  db.Model.metadata,
  db.Column('post_id', db.ForeignKey('posts.id'), primary_key=True),
  db.Column('category_id', db.ForeignKey('categories.id'), primary_key=True),
  extend_existing=True,
)

class User(db.Model, SerializerMixin):
  __tablename__ = 'users'
  
  serialize_rules = ('-posts',)
  
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String, nullable = False, unique = True)
  email = db.Column(db.String, nullable = False, unique = True)
  mobile_number = db.Column(db.Integer, nullable = False, unique = True)
  
  posts = db.relationship('Post', backref = db.backref('user'))
  
  def __repr__(self):
    return f"""
      id: {self.id}
      username: {self.username}
      email: {self.email}
      mobile_number: {self.mobile_number}
    """
  
class Post(db.Model, SerializerMixin):
  __tablename__ = 'posts'
  
  serialize_rules = ('-categories.posts','-user.posts')
  
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String, nullable = False, unique = True)
  body = db.Column(db.String)
  created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
  updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  
  categories = db.relationship("Category", secondary=post_category, backref=db.backref('posts'))
  
  def __repr__(self):
    return f"""
      id: {self.id}
      title: {self.title}
      body: {self.body}
      user_id: {self.user_id}
    """
  
class Category(db.Model, SerializerMixin):
  __tablename__ = 'categories'
  
  serialize_rules = ('-posts.categories',)
  
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String, nullable = False, unique = True)
  # posts = db.relationship("Post", secondary=post_category, backref=db.backref('categories'))
  
  def __repr__(self):
    return f"""
      id: {self.id}
      title: {self.title}
    """
  
  