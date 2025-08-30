from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User 
 
@app.route('/')
<<<<<<< HEAD
@app.route('/home') 
def index(): 
    return render_template('index.html', title='Home', total_properties=properties)
=======
@app.route('/index') 
@login_required 
def index(): 
    user = {'username': 'Miguel'}
    posts = [ 
        { 
            'author': {'username': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        }, 
        { 
            'author': {'username': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        } 
    ] 
    return render_template("index.html", title='Home Page', posts=posts)
>>>>>>> a70ddfc4ac94acdbe249e7f44b6f630222d8d850

@app.route('/login', methods=['GET', 'POST']) 
def login(): 
    if current_user.is_authenticated: 
        return redirect(url_for('index')) 
    form = LoginForm() 
    if form.validate_on_submit(): 
        user = User.query.filter_by(username=form.username.data).first() 
        if user is None or not user.check_password(form.password.data): 
            flash('Invalid username or password') 
            return redirect(url_for('login')) 
        login_user(user, remember=form.remember_me.data) 
        next_page = request.args.get('next') 
        if not next_page or url_parse(next_page).netloc != '': 
            next_page = url_for('index') 
        return redirect(next_page) 
    return render_template('login.html', title='Sign In', form=form) 

@app.route('/logout') 
def logout(): 
    logout_user() 
    return redirect(url_for('index')) 

@app.route('/register', methods=['GET', 'POST']) 
def register(): 
    if current_user.is_authenticated: 
        return redirect(url_for('index')) 
    form = RegistrationForm() 
    if form.validate_on_submit(): 
        user = User(
            username=form.username.data,
            email=form.email.data,
            acc_type=form.acc_type.data  # Make sure your form provides this!
        )
        user.set_password(form.password.data) 
        db.session.add(user) 
        db.session.commit() 
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login')) 
    return render_template('register.html', title='Register', form=form)