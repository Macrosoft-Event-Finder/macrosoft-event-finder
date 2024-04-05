from flask import Flask, Blueprint, render_template, request, flash, session, redirect, url_for
from datetime import datetime
from langdetect import detect
from . import main
from .forms import EventForm
from .. import db
from ..models import User
from flask_login import login_required

@main.route('/', methods=['GET','POST'])
#@login_required
def homepage():
    return render_template('homepage.html')
	  
@main.route('/create_event',methods=['GET','POST'])
@login_required
def create_event():
    eventForm = EventForm()
    return render_template('create_event.html', eventForm=eventForm)

