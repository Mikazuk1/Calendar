from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateTimeLocalField
from wtforms.validators import DataRequired, Email, ValidationError
from datetime import datetime

# class ValidDateTime(object):
#     def __init__(self, message=None):
#         if not message:
#             message = 'Invalid datetime format'
#         self.message = message

#     def __call__(self, form, field):
#         if not field.data:
#             raise ValidationError('Date and time must be provided')
#         try:
#             datetime.strptime(field.data, '%Y-%m-%dT%H:%M:%S')  # Include seconds in the format
#         except ValueError:
#             raise ValidationError(self.message)

class AddEvent(FlaskForm):
    applicant = StringField('Enter Name', validators=[DataRequired()])
    event_name = StringField('Enter Title', validators=[DataRequired()])
    facility = StringField('Enter Facility', validators=[DataRequired()])
    startdate = DateTimeLocalField('Starting Date', format='%Y-%m-%dT%H:%M',validators=[DataRequired()])
    enddate = DateTimeLocalField('End Date', format='%Y-%m-%dT%H:%M',validators=[DataRequired()])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')