#!/usr/bin/env python3

from faker import Faker

from app import app
from models import db, User, Post, Category

# fake = Faker()
# print(fake.domain_name())

with app.app_context():
    
    fake = Faker()

    User.query.delete()
    Post.query.delete()
    Category.query.delete()

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
    
    posts = []
    for u in users:
      post = Post(
        title = fake.text(max_nb_chars=20).title(),
        body = fake.paragraph(nb_sentences=5),
        user_id=u.id
      )
      
      posts.append(post)
    
    db.session.add_all(posts)
    db.session.commit()
  
    categories = []
    for i in range(5):
      category = Category(
        title=fake.word().title()
      )
      categories.append(category)
      
    db.session.add_all(categories)
    db.session.commit()
    


    