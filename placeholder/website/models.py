from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from website import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from website import login_manager


#the join table. Establishes many to many relationship between users and events
event_user=db.Table('event_user',
    db.Column('user_id',db.Integer,db.ForeignKey('user.id')),
    db.Column('event_id',db.Integer,db.ForeignKey('event.id')))  

#the User table with login functionalities
class User(UserMixin, db.Model):
    __tablename__='user'
    id=db.Column(db.Integer, primary_key=True)
    
    email=db.Column(db.String,unique=True)
    password=db.Column(db.String)
    password_hash = db.Column(db.String(128))
    first_name=db.Column(db.String)
    last_name=db.Column(db.String)
    
    account_balance=db.Column(db.Numeric(precision=15,scale=2),default=0)
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    def __repr__(self):
        return '<User %r>' %self.email

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#event table 
class Event(db.Model):
     __tablename__='event'
     #establish many events to one category
     event_category_id=db.Column(db.Integer, db.ForeignKey('event_categories.id'))
     users=db.relationship('User',secondary=event_user,backref='events')
     id=db.Column(db.Integer, primary_key=True)
     title=db.Column(db.String)
     description=db.Column(db.Text)
     flier_image_path=db.Column(db.String(255), default='default_image.jpg') #it is not efficient to store images directly in database, we must store the path to the image instead. We can also create a default value for the image
     capacity=db.Column(db.Integer)
     location=db.Column(db.String)
     paymentRequired=db.Column(db.Boolean, default=False)
     paymentAmount=db.Column(db.Integer, default=0)
     start_date=db.Column(db.Date)
     start_time=db.Column(db.Time)
     end_date=db.Column(db.Date)
     end_time=db.Column(db.Time)

class EventCategories(db.Model):
     __tablename__='event_categories'
     id=db.Column(db.Integer, primary_key=True)
     event_category=db.Column(db.String)
    #establish many events to one category
     events=db.relationship('Event',backref='category')

class EventOrganizer(db.Model):
    __tablename__='event_organizers'
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))
    event_id=db.Column(db.Integer,db.ForeignKey('event.id'))
    is_organizer=db.Column(db.Boolean,default=False)
    
'''
One category has many events but one event can only have one category. 
If you want events to have multiple categories, you can possibly have 
an intermediary table to establish many to many relationship.
'''




