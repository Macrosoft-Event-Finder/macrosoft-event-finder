from flask import Flask, Blueprint, app, render_template, request, flash, session, redirect, url_for, request
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from langdetect import detect
from . import main
from .forms import EventForm
from .. import db
from ..models import User, Event, EventCategories
from flask_login import login_required

@main.route('/', methods=['GET','POST'])
#@login_required
def homepage():
    events = Event.query.order_by(Event.start_date).all()
    return render_template('homepage.html', events=events)
	  
@main.route('/create_event',methods=['GET','POST'])
@login_required
def create_event():
    eventForm = EventForm()

    if eventForm.validate_on_submit():
        event = Event(
            title = eventForm.title.data,
            description = eventForm.description.data,
            capacity = eventForm.capacity.data,
            location = eventForm.location.data,
            start_date = eventForm.start_date.data,
            end_date = eventForm.end_date.data,
            start_time = eventForm.start_time.data,
            end_time = eventForm.end_time.data,
            #flier_image_path= eventForm.flier_image_path.data,
            paymentRequired = eventForm.paymentRequired.data,
            paymentAmount = eventForm.paymentAmount.data,
        )
        db.session.add(event)
        db.session.commit()

        category = EventCategories(
            event_category = eventForm.event_category.data,
        )
        db.session.add(category)
        db.session.commit()

        flash('Event posted.')
        return redirect(url_for('main.homepage'))
    return render_template('create_event.html', eventForm=eventForm)

