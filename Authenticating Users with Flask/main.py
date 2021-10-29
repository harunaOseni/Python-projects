from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from decouple import config

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['FLASK_FILE'] = r'C:\Users\oseni haruna\OneDrive\Documents\Python Programming\Day68\Authenticating Users with Flask\static\files'
app.secret_key = config('SECRET_KEY')
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

# CREATE TABLE IN DB


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
# Line below only required once, when creating DB.
# db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = generate_password_hash(
            password=request.form["password"], method="pbkdf2:sha256", salt_length=8)
        user = User(name=name, email=email, password=password)
        db.session.add(user)e
        db.session.commit()
        return redirect(url_for('secrets', name=name.split()[0]))
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(pwhash=user.password, password=password):
            login_user(user)
            return redirect(url_for('secrets', name=user.name.split()[0], logged_in=True))
        else:
            flash("Please check your email and password")
    return render_template("login.html", logged_in=False)


@app.route('/secrets')
@login_required
def secrets():
    if current_user.is_authenticated:
        return render_template("secrets.html", name=current_user.name.split()[0])


@app.route('/logout')
@login_required
def logout():
    if current_user.is_authenticated:
        return logout_user()
    else:
        return flash("You are not logged in")


@app.route('/download')
@login_required
def download():
    if current_user.is_authenticated:
        return send_from_directory(app.config['FLASK_FILE'], path='cheat_sheet.pdf', as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
