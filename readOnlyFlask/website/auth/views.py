from flask import Flask, Blueprint, render_template, request, flash, session, redirect, url_for
from . import auth
from .forms import RegistrationForm
from ..models import User
from ..models import db
@auth.route('/login')
def login():
    return render_template('auth/login.html')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    registrationForm = RegistrationForm()
    if registrationForm.validate_on_submit():
        user = User(email=registrationForm.email.data,
                    username=registrationForm.username.data,
                    password=registrationForm.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You can now login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', registrationForm=registrationForm)