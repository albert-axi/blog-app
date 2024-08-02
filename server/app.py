#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import User, Post, Category

# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'
  
@app.route('/users', methods = ['GET', 'POST'])
def all_users():
  
  if request.method == 'GET':
    users = User.query.all()
    user_list = [u.to_dict() for u in users]
    
    return make_response(user_list, 200)
  elif request.method == 'POST':
    user = User(
      username = request.json['username'],
      email = request.json['email'],
      mobile_number = request.json['mobile_number']
    )
    
    db.session.add(user)
    db.session.commit()
    
    return make_response(user.to_dict(), 200)
  
@app.route('/users/<int:id>', methods=['GET', 'PATCH','DELETE'])
def user_by_id(id):
  user = User.query.filter(User.id == id).first()

  if not user:
    return make_response({"message": "No user found!"}, 200)
  
  if request.method == 'GET':
    return make_response(user.to_dict(), 200)
  elif request.method == 'PATCH':
    for (k,v) in request.json.items():
      setattr(user, k, v)
    db.session.add(user)
    db.session.commit()
    
    return make_response(user.to_dict(), 200)
  elif request.method == 'DELETE':
    db.session.delete(user)
    db.session.commit()
    
    return make_response({'message': f"Successfully deleted user with id of {user.id}"}, 200)

@app.route("/users/<int:id>/posts", methods=['GET', 'POST'])
def user_posts_by_id(id):
  user = User.query.filter(User.id == id).first()
  
  if not user:
    return make_response({"message": "No user found!"}, 200)
  
  if request.method == 'GET':
    posts = [ p.to_dict() for p in user.posts]
    return make_response(posts, 200)
  elif request.method == 'POST':
    post = Post(
      title = request.json['title'],
      body = request.json['body'],
      user_id = id
    )
    
    db.session.add(post)
    db.session.commit()
    
    return make_response(post.to_dict(), 200)
    
  
  
  
  
    
@app.route('/posts')
def all_posts():
  posts = Post.query.all()
  post_list = [p.to_dict() for p in posts]
  
  return make_response(post_list, 200)

@app.route('/categories')
def all_categories():
  categories = Category.query.all()
  category_list = [c.to_dict() for c in categories]
  
  return make_response(category_list, 200)

if __name__ == '__main__':
    app.run(port=5555, debug=True)