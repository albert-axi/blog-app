#!/usr/bin/env python3

from faker import Faker
import random

from app import app
from models import db, User, Post, Category,post_category

# fake = Faker()
# print(fake.domain_name())

with app.app_context():
    
    fake = Faker()

    User.query.delete()
    Post.query.delete()
    Category.query.delete()
    # post_category.query.delete()

    users = []
    for i in range(5):
        name = fake.unique.first_name().lower()
        user = User(
            username = name,
            email = f"{name}@{fake.domain_name()}",
            mobile_number = fake.phone_number()
        )
        users.append(user)

    db.session.add_all(users)
    db.session.commit()
    
    categories = []
    for i in range(5):
      category = Category(
        title=fake.word().title()
      )
      categories.append(category)
      
    db.session.add_all(categories)
    db.session.commit()
    
    posts = []
    for u in users:
      for i in range(5):
        post = Post(
          title = fake.text(max_nb_chars=20).title(),
          body = fake.paragraph(nb_sentences=5),
        )
        post.user = u
        for i in range(random.randint(0,3)):
          category = random.choice(categories)
          post.categories.append(category)
        
        posts.append(post)
    
    db.session.add_all(posts)
    db.session.commit()
    print(posts)
  
    


    