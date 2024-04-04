from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length

class HindiInputForm(FlaskForm):
    hindiInput=TextAreaField('Input Hindi Text Here', validators=[DataRequired()])
    submit=SubmitField('Submit')

class LoginForm(FlaskForm):
    username=StringField('Enter Username:', validators=[DataRequired()])
    password=PasswordField('Enter password:', validators=[DataRequired(), Length(8,64)])
    remember_me=BooleanField('Remember Me')
    submit=SubmitField('Submit')

class SignUpForm(FlaskForm):
    username=TextAreaField('Create a UserName', validators=[DataRequired()])
    password=TextAreaField('Create a PassWord',validators=[DataRequired()])
    submit=SubmitField('Submit')