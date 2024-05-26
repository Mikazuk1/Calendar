from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm, AddEvent
from datetime import datetime
from flask_login import LoginManager, UserMixin

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
    time_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Sched {self.id}>'
 
 
 
@app.route("/")
@app.route("/home")
def home():
    page = request.args.get('page', 1, type = int)
    events = Sched.query.order_by(Sched.applicant.desc()).paginate(page = page , per_page = 4)
    return render_template('home.html', title='Home', events=events)

@app.route("/latest")
def latest():
    page = request.args.get('page', 1, type = int)
    events = Sched.query.order_by(Sched.time_posted.desc()).paginate(page = page , per_page = 4)
    return render_template('latest.html', title='Latest', events=events)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
         if form.email.data == 'admin@cjc.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
         else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    return render_template("/home")



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
            flash('Schedule Created', 'success')
            return redirect(url_for('home'))
    return render_template("addevent.html", title="Create Event", legend = "Create Schedule" ,form=form)

@app.route("/calendar")
def calendar():
    events = Sched.query.all()
    return render_template("calendar.html", events = events)

@app.route("/sched/<int:id>")
def sched(id):
    event = Sched.query.get_or_404(id)
    return render_template("sched.html", title = event.event_name ,event = event)


@app.route("/sched/<int:id>/update", methods=['GET','POST'])
def updatesched(id):
    event = Sched.query.get_or_404(id)
    form = AddEvent()
    if form.validate_on_submit():
        event.applicant = form.applicant.data
        event.event_name = form.event_name.data
        event.facility = form.facility.data
        event.startdate = form.startdate.data
        event.enddate = form.enddate.data
        db.session.commit()
        flash('Schedule Updated', 'success')
        return redirect(url_for('sched',id=event.id))
    elif request.method == "GET":
        form.applicant.data = event.applicant
        form.event_name.data = event.event_name
        form.facility.data = event.facility
    return render_template('addevent.html',title="Update Schedule",form=form,legend="Update Schedule")

@app.route("/sched/<int:id>/delete", methods=['POST'])
def delete_sched(id):
    event = Sched.query.get_or_404(id)
    db.session.delete(event)
    db.session.commit()
    flash('Schedule Deleted!','success')
    return redirect(url_for('home'))

@app.route("/applicant/<string:applicant>")
def applicant_name(applicant):
    page = request.args.get('page', 1, type = int)
    events = Sched.query.filter_by( applicant = applicant ).order_by(Sched.startdate.desc()).paginate(page = page , per_page = 4)
    return render_template('applicant_name.html', events=events, applicant=applicant)

    

if __name__ == '__main__':
    app.run(debug=True)


    