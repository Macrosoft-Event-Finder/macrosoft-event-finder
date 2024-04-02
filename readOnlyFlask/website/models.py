from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from website import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from website import login_manager

class User(UserMixin, db.Model):
    __tablename__='users'
    id=db.Column(db.Integer, primary_key=True)
    
    username=db.Column(db.String(32), unique=True)
    password=db.Column(db.String)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    pastInputs=db.relationship('PastInput',backref='user', order_by='PastInput.dateCreated')
    def __repr__(self):
        return '<User %r>' %self.username

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class PastInput(db.Model):
    __tablename__='pastInputs'
    id=db.Column(db.Integer, primary_key=True)
    pastInput=db.Column(db.Text)
    dateCreated=db.Column(db.DateTime)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    def __repr__(self):
        return '<Input %r>' % self.pastInput
    
class User(db.Model):
        __tablename__='users'
        userId=db.Column(db.Integer,primary_key=True)
        firstName=db.Column(db.String)
        lastName=db.Column(db.String)
        email=db.Column(db.String)
        password=db.Column(db.String)
        accountBalance=db.Column(db.Numeric(precision=15,scale=2),default=0)

class UnionTable(db.Model):
        __tablename__='union_table'
        eventId=db.Column(db.Integer)
        userId=db.Column(db.Integer)
        isOrganizer=db.Column(db.Boolean)

class Event(db.Model):
     __tablename__='events'
     #establish many events to one category
     event_category_id=db.Column(db.Integer, db.ForeignKey('event_category.id'))

     eventID=db.Column(db.Integer)
     description=db.Column(db.Text)
     flier_image_path=db.Column(db.String(255)) #it is not efficient to store images directly in database, we must store the path to the image instead
     capacity=db.Column(db.Integer)
     location=db.Column(db.String)
     isPaidOnly=db.Column(db.Boolean)
     startDate=db.Column(db.DateTime)
     endDate=db.Column(db.DateTime)

class EventCategories(db.Model):
     __tablename__='event_categories'
     id=db.Column(db.Integer, primary_key=True)
     event_category=db.Column(db.String)
    #establish many events to one category
     events=db.relationship('Event',backref='category')
'''
One category has many events but one event can only have one category. 
If you want events to have multiple categories, you can possibly have 
an intermediary table to establish many to many relationship.
'''




