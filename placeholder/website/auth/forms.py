from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),Email()])
    password = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Re-enter Password', validators=[DataRequired()])
    first_name=StringField('First Name', validators=[DataRequired(),Length(1,64),Regexp('^[A-Z][a-z]*$'
, message='Enter your name in regular format, first letter capital, the rest lowercase')])
    last_name=StringField('Last Name',validators=[DataRequired(),Length(1,64),Regexp('^[A-Z][a-z]*$'
, message='Enter your name in regular format, first letter capital, the rest lowercase')])
    submit = SubmitField('Register')

    def validate_email_field(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('This email is already in use.')

class LoginForm(FlaskForm):
    email=StringField('Enter Email:', validators=[DataRequired(), Email()])
    password=PasswordField('Enter password:', validators=[DataRequired(), Length(8,64)])
    remember_me=BooleanField('Remember Me')
    submit=SubmitField('Submit')
