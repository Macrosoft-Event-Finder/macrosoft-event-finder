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