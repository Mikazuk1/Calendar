from flask import Flask, render_template, url_for, flash, redirect
import mysql.connector
from forms import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY']='6a8ed0da5ab41df512731f11f479b01d'
# conn = mysql.connector.connect(host='localhost',user='root',password='lolislife23',database='calendar')

events = [
    {
        'eventID':'E-1', 
        'applicant': 'Nicki',
        'title': 'CCIS PARTY',
        'facilities': 'Edtect Hall',
        'starttime':'1:00 PM',
        'endtime': '3:00 PM',
        'date': '2024-05-05'
    },
    {
        'eventID':'E-1', 
        'applicant': 'philip',
        'title': 'Pasko',
        'facilities': 'Edtect Hall',
        'starttime':'1:00 PM',
        'endtime': '3:00 PM',
        'date': '2024-05-06'
    },
    {
        'eventID':'E-2',
        'applicant': 'Alexis',
        'title': 'Meeting de avance',
        'facilities': 'GYM',
        'starttime':'9:00 AM',
        'endtime':'1:30 PM',
        'date': '2024-06-05'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',events=events)

@app.route("/calendar")
def calendar():
    return render_template("calendar.html", events = events)

@app.route("/addevent")
def addevent():
    return render_template("addevent.html")
    
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@cjc.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)