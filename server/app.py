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
  
@app.route('/users')
def all_users():
  users = User.query.all()
  user_list = [u.to_dict() for u in users]
  
  return make_response(user_list, 200)

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