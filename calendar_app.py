from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm, AddEvent
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY']='6a8ed0da5ab41df512731f11f479b01d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:lolislife23@localhost/calendar_db'
db =SQLAlchemy(app)

class Event(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    applicant = db.Column(db.String(50),unique=True,nullable=False)
    event = db.Column(db.String(50),unique=True,nullable=False)
    facility = db.Column(db.String(50),unique=True,nullable=False)
    # starttime = db.Column(db.DateTime,nullable=False)
    # endtime = db.Column(db.DateTime,nullable=False)
    startdate = db.Column(db.DateTime, nullable=False)
    enddate = db.Column(db.DateTime, nullable=False)
    def __repr__(self):
        return f"Applicant '{self.applicant}', Event'{self.title}', Facility'{self.facility}', Date'{self.date}'"
    
    

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

@app.route("/addevent", methods=['GET','POST'])
def addevent():
    form = AddEvent()
    return render_template("addevent.html",title="Calendar Schedules",form=form)

@app.route("/")
@app.route("/home")
def home():
    events = Event.query.all()
    return render_template('home.html',events=events)

@app.route("/calendar")
def calendar():
    events = Event.query.all()
    return render_template("calendar.html", events = events)



if __name__ == '__main__':
    app.run(debug=True)