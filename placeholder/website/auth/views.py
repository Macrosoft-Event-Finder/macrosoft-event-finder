from flask import Flask, Blueprint, render_template, request, flash, session, redirect, url_for
from . import auth
from .forms import RegistrationForm, LoginForm
from ..models import User
from ..models import db
from flask_login import login_required, login_user, logout_user

@auth.route('/login',methods=['GET','POST'])
def login():
    loginForm=LoginForm()
    if loginForm.validate_on_submit():  
        user=User.query.filter_by(email=loginForm.email.data).first()
        if user is not None and user.verify_password(loginForm.password.data):
            login_user(user, loginForm.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('auth.login')
            return redirect(next)
        flash('Invalid username or password.')
    return render_template('homepage.html')#render_template('auth/login.html', loginForm=loginForm, email=session.get('email'), password=session.get('password'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    registrationForm = RegistrationForm()
    if registrationForm.validate_on_submit():
        user = User(email=registrationForm.email.data,
                    password=registrationForm.password.data,
                    first_name=registrationForm.first_name.data,
                    last_name=registrationForm.last_name.data)
        db.session.add(user)
        db.session.commit()
        flash('You can now login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', registrationForm=registrationForm)