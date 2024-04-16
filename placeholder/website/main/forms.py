from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, BooleanField, SelectField, DateField,FileField, TimeField, IntegerField, validators
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from flask_wtf.file import FileField, FileAllowed

class EventForm(FlaskForm):
    title=StringField('Enter event title',validators=[DataRequired()], render_kw={"placeholder": "Enter event title", "class": "input-field"})
    description=TextAreaField('Enter event description', validators=[DataRequired()], render_kw={"placeholder": "Enter event description", "class": "input-field"})
    capacity=IntegerField('Enter capacity', validators=[DataRequired()], render_kw={"placeholder": "Enter capacity", "class": "input-field"})

    location=StringField('Enter location', validators=[DataRequired()], render_kw={"placeholder": "Enter capacity", "class": "input-field"})
    
    start_date=DateField('Event start date (dd/mm/yyyy)', validators=[DataRequired()]) #render_kw={"placeholder": "DD/MM/YYYY"})
    end_date = DateField('Event end date (dd/mm/yyyy)', validators=[DataRequired()])

    start_time = TimeField('Event start time (hour:minute am/pm)', validators=[DataRequired()])
    end_time = TimeField('Event end time (hour:minute am/pm)', validators=[DataRequired()])

    flier_image_path=FileField('Upload flier for event', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    
    paymentRequired = BooleanField('Is the event payment required?', validators=[validators.optional()])
    paymentAmount = IntegerField('If payment required, enter payment amount', validators=[validators.Optional(), validators.NumberRange(min=0)])
    event_category=SelectField('Select the category that best fits your event',validators=[DataRequired()],
                               choices=[('social', 'Social'),
                                          ('educational', 'Educational'),
                                          ('fine_arts_media', 'Fine Arts and Media'),
                                          ('fundraiser', 'Fundraiser'),
                                          ('meeting', 'Meeting'),
                                          ('service_volunteer', 'Service/Volunteer'),
                                          ('speaker_lecturer', 'Speaker/Lecturer'),
                                          ('recreational', 'Recreational'),
                                          ('other', 'Other'),])
    
    post_event=SubmitField('Post Event')