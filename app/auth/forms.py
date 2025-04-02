from flask_wtf import FlaskForm
from flask_babel import _, lazy_gettext as _l
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app import db
import sqlalchemy as sa
from app.models import User

class LoginForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    remember_me = BooleanField(_l('Remember Me'))
    submit = SubmitField(_l('Sign in'))

class RegistrationForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    password2 = PasswordField(
        _l('Repeat Password'), validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('Register'))
    
    def validate_username(self, username):
        user = db.session.scalar(
            sa.select(User).where(User.username == username.data))
        if user is not None:
            raise ValidationError(_l('Please use a different username.'))
    
    def validate_email(self, email):
        user = db.session.scalar(
            sa.select(User).where(User.email == email.data))
        if user is not None:
            raise ValidationError(_l('Please use a different email adress.'))

class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('Submit'))

class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    password2 = PasswordField(
        _l('Repeat Password'), validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField(_l('Request Password Reset'))
