
"""The views module.

This module contain all of the routes for the application.
"""
from group_blog import app
from flask import render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@smallgroup.com' and form.password.data == 'password':
            flash('You have been logged in sucessfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check credentials', 'danger')
    return render_template('login.html', title='Login', form=form)