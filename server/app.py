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

if __name__ == '__main__':
    app.run(port=5555, debug=True)