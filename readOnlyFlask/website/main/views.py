from flask import Flask, Blueprint, render_template, request, flash, session, redirect, url_for
from datetime import datetime
from langdetect import detect
from . import main
from .forms import HindiInputForm, LoginForm
from .. import db
from ..models import User, PastInput
from flask_login import login_required, login_user, logout_user
@main.route('/', methods=['GET','POST'])
@login_required
def readOnly():
    
    form=HindiInputForm()
    
    if form.validate_on_submit():  
        hindiInput1=session.get('hindiInput') 
        lang=detect(hindiInput1)
        if lang!='hi':
            flash("This Program Only Works for Hindi Text")
        else:
            flash("Let's Read Some Hindi!")
        session['hindiInput']=form.hindiInput.data
        return redirect(url_for('main.readOnly'))
    return render_template('readOnly.html', current_time=datetime.utcnow(), form=form, hindiInput=session.get('hindiInput'))
	
'''
    if request.method=='POST':
        hindiUserInput=request.form.get('hindiUserInput')
        
        
        form=hindiUserInput()
   
        return redirect(url_for('readOnly'))  
    
    return render_template('readOnly.html',current_time=datetime.utcnow())
'''  
@main.route('/readOnlyMode')
@login_required
def readOnlyMode():
    return render_template('readOnlyMode.html')

@main.route('/login',methods=['GET','POST'])
def login():
    loginForm=LoginForm()
    if loginForm.validate_on_submit():  
        user=User.query.filter_by(username=loginForm.username.data).first()
        if user is not None and user.verify_password(loginForm.password.data):
            login_user(user, loginForm.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.login')
            return redirect(next)
        flash('Invalid username or password.')
    return render_template('login.html', loginForm=loginForm, username=session.get('username'), password=session.get('password'))
@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.login'))