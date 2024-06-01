from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateTimeLocalField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class AddEvent(FlaskForm):
    applicant = StringField('Enter Name', validators=[DataRequired()])
    event_name = StringField('Enter Title', validators=[DataRequired()])
    facility = StringField('Enter Facility', validators=[DataRequired()])
    startdate = DateTimeLocalField('Starting Date', format='%Y-%m-%dT%H:%M',validators=[DataRequired()])
    enddate = DateTimeLocalField('End Date', format='%Y-%m-%dT%H:%M',validators=[DataRequired()])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')