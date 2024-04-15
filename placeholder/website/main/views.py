from flask import Flask, Blueprint, app, render_template, request, flash, session, redirect, url_for, request, jsonify
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from langdetect import detect
from . import main
from .forms import EventForm
from .. import db
from ..models import User, Event, EventCategories
from flask_login import login_required
import stripe

# secret key for testing
stripe.api_key = 'sk_test_51P4ASURrWMk3kdo0BdbeZPRHlrYf4zoV2uCfURSXZZ84Yjk5ljYqDoB5sWYRhHescaAoVYLT9kDY3ODkRMYHAzqV009qCEuOyz'

@main.route('/', methods=['GET','POST'])
#@login_required
def homepage():
    events = Event.query.order_by(Event.start_date).all()
    return render_template('homepage.html', events=events)

@main.route('/event_page', methods=['GET','POST'])
def event_page():
    events = Event.query.all()
    
    event = Event(  )
    
    return render_template('event_page.html', events=events)

@main.route('/create_event', methods=['GET','POST'])
@login_required
def create_event():
    eventForm = EventForm()

    
    if eventForm.validate_on_submit():
        category = EventCategories(
            event_category = eventForm.event_category.data,
        )
        db.session.add(category)
        db.session.commit()

        if eventForm.paymentAmount.data is None:
            eventForm.paymentAmount.data = 0
        event = Event(
            title = eventForm.title.data,
            description = eventForm.description.data,
            capacity = eventForm.capacity.data,
            location = eventForm.location.data,
            start_date = eventForm.start_date.data,
            end_date = eventForm.end_date.data,
            start_time = eventForm.start_time.data,
            end_time = eventForm.end_time.data,
            flier_image_path = 'img1.jpg',
            paymentRequired = eventForm.paymentRequired.data,
            paymentAmount = eventForm.paymentAmount.data,
        )
        db.session.add(event)
        db.session.commit()

        flash('Event posted.')
        return redirect(url_for('main.homepage'))
    return render_template('create_event.html', eventForm=eventForm)

@main.route("/config")
def get_publishable_key():
    stripe_config = {"publicKey": "pk_test_51P4ASURrWMk3kdo04r3ahTD308dHHV5EeELFbVOZ6ihR9t3iCBIe7o98vlvzBS7MQVJqklW1xsjxT7VUuT98T1N500aHs2qBfv"}
    return jsonify(stripe_config)

@main.route('/create-checkout-session')
@login_required
def create_checkout_session():
    domain_url = "http://127.0.0.1:5000/"
    stripe.api_key = "sk_test_51P4ASURrWMk3kdo0BdbeZPRHlrYf4zoV2uCfURSXZZ84Yjk5ljYqDoB5sWYRhHescaAoVYLT9kDY3ODkRMYHAzqV009qCEuOyz"

    try:
        # Create new Checkout Session for the order
        # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
        checkout_session = stripe.checkout.Session.create(
            success_url=domain_url + "success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=domain_url + "cancelled",
            payment_method_types=["card"],
            mode="payment",
            line_items=[
                {
                    "price": "price_1P4RJRRrWMk3kdo09puS8hin",
                    "quantity": 1,
                }
            ]
        )
        return jsonify({"sessionId": checkout_session["id"]})
    except Exception as e:
        return jsonify(error=str(e)), 403

@main.route("/success")
def success():
    return render_template("success.html")

@main.route("/cancelled")
def cancelled():
    return render_template("cancelled.html")

if __name__ == '__main__':
    main.run()
