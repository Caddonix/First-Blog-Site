from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm (FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=6, max=16)])
    email = StringField('Email', validators=[DataRequired(), 
                        Email()])
    password = PasswordField('Password', validators=[DataRequired(), ])
    confirmPassword = PasswordField('Confirm Password', validators=[
                                    DataRequired(), EqualTo('Password')])
    submit = SubmitField('Sign Up')

class LoginForm (FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')