from flask import render_template, redirect, flash, url_for
from app import app, db
from app.forms import LoginForm
from flask_login import current_user, login_user
import sqlalchemy as sa
from app.models import User

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Warell'}
    posts = [
        {
            'author': {'username': 'Warell'},
            'body': 'Un día fantástico para programar'
        },
        {
            'author': {'username': 'Lesomio'},
            'body': 'Me encanta jugar al rocket leage'
        },
        {
            'author': {'username': 'Totonio'},
            'body': 'No me gusta el futbol'
        }
    ]
    return render_template('index.html', title='Home Page', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign in', form=form)    

