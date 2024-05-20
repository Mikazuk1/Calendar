from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm, AddEvent
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:lolislife23@localhost/calendar_db'
db = SQLAlchemy(app)

class Sched(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applicant = db.Column(db.String(50),unique=False, nullable=False)
    event_name = db.Column(db.String(50),unique=False, nullable=False)
    facility = db.Column(db.String(50),unique=False, nullable=False)
    startdate = db.Column(db.String(50), nullable=False)
    enddate = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return f'<Sched {self.id}>'

@app.route("/addevent", methods=['GET','POST'])
def addevent():
    form = AddEvent()
    if request.method == "POST":
        if form.validate_on_submit():
            new_sched = Sched(
                applicant=form.applicant.data,
                event_name=form.event_name.data,
                facility=form.facility.data,
                startdate=form.startdate.data,
                enddate=form.enddate.data
            )
            db.session.add(new_sched)
            db.session.commit()
            flash("Schedule Created", "success")
            return redirect(url_for('home'))
    return render_template("addevent.html", title="Create Event", form=form)

@app.route("/calendar")
def calendar():
    events = Sched.query.all()
    return render_template("calendar.html", events = events)


@app.route("/")
@app.route("/home")
def home():
    events = Sched.query.all()
    return render_template('home.html', title='Home', events=events)

if __name__ == '__main__':
    app.run(debug=True)
