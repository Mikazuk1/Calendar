from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField
from wtforms.validators import DataRequired, Email

class AddEvent(FlaskForm):
    event = StringField('Enter Title', validators=[DataRequired()])
    applicant = StringField('Enter Title', validators=[DataRequired()])
    facility = StringField('Enter Title', validators=[DataRequired()])
    startdate = DateField('Starting Date', validators=[DataRequired()])
    enddate = DateField('End Date', validators=[DataRequired()])

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')