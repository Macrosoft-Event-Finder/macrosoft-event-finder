from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, BooleanField, SelectField, DateTimeField,FileField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo



class EventForm(FlaskForm):
    event_title=StringField('Enter event title',validators=[DataRequired()])
    description=TextAreaField('Enter event description', validators=[DataRequired()])
    start_date=DateTimeField('Event start time')
    end_date=DateTimeField('Event end time')
    flier_image_path=FileField('Upload flier for event')
    event_category=SelectField('Select the category that best fits your event',['Social','Educational','Fine Arts and Media','Fundraiser','Meeting','Other','Service/Volunteer', 'Speaker/Lecturer','Recreational'])
    post_event=SubmitField('Post Event')