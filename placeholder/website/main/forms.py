from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, BooleanField, SelectField, DateField,FileField, TimeField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo



class EventForm(FlaskForm):
    event_title=StringField('Enter event title',validators=[DataRequired()], render_kw={"placeholder": "Enter event title", "class": "input-field"})
    description=TextAreaField('Enter event description', validators=[DataRequired()], render_kw={"placeholder": "Enter event description", "class": "input-field"})
    
    start_date=DateField('Event start date (dd/mm/yyyy)', format='%d/%m/%Y') #render_kw={"placeholder": "DD/MM/YYYY"})
    start_time = TimeField('Event start time (hour:minute am/pm)', format='%I:%M %p', validators=[DataRequired()])
    end_date = DateField('Event end date (dd/mm/yyyy)', format='%d/%m/%Y', validators=[DataRequired()])
    end_time = TimeField('Event end time (hour:minute am/pm)', format='%I:%M %p', validators=[DataRequired()])

    flier_image_path=FileField('Upload flier for event')
    event_category=SelectField('Select the category that best fits your event',choices=[('social', 'Social'),
                                          ('educational', 'Educational'),
                                          ('fine_arts_media', 'Fine Arts and Media'),
                                          ('fundraiser', 'Fundraiser'),
                                          ('meeting', 'Meeting'),
                                          ('other', 'Other'),
                                          ('service_volunteer', 'Service/Volunteer'),
                                          ('speaker_lecturer', 'Speaker/Lecturer'),
                                          ('recreational', 'Recreational')])
    post_event=SubmitField('Post Event')