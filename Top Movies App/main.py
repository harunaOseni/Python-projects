from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
MOVIE_API_KEY = '5ec57ed8064b451a2014b714c191cb23'
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True)
    year = db.Column(db.Integer)
    description = db.Column(db.String(250))
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(250))
    img_url = db.Column(db.String(250))


class RatingForm(FlaskForm):
    rating = StringField('Your Rating Out of 10 e.g 7.5',
                         validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    submit = SubmitField('Submit')


class SearchForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Submit')


db.create_all()


@app.route("/")
def home():
    movies = Movie.query.order_by(Movie.rating.asc()).all()
    descending_movies = Movie.query.order_by(Movie.rating.desc()).all()
    for movie in descending_movies:
        movie.ranking = descending_movies.index(movie) + 1
    return render_template('index.html', movies=movies)


@app.route("/edit/<int:movie_id>", methods=["GET", "POST", "PUT"])
def edit(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    form = RatingForm()
    if request.method == "POST":
        if form.validate_on_submit():
            movie.rating = form.rating.data
            movie.review = form.review.data
            db.session.commit()
            return redirect(url_for("home", movies=Movie.query.all()))
    else:
        return render_template("edit.html", movie=movie, form=form)


@app.route("/delete/<int:movie_id>")
def delete(movie_id):
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home', movies=Movie.query.all()))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = SearchForm()
    if request.method == "POST":
        if form.validate_on_submit():
            title = form.title.data
            # searcj for movie in TMDB
            request_url = f"https://api.themoviedb.org/3/search/movie?api_key={MOVIE_API_KEY}&query={title}"
            response = requests.get(request_url)
            results = response.json()['results']
            if results:
                return render_template("select.html", results=results)
    else:
        return render_template("add.html", form=form)


@app.route("/select/<int:movie_id>", methods=["GET", "POST"])
def select(movie_id):
    request_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={MOVIE_API_KEY}&append_to_response=credits,videos,images"
    response = requests.get(request_url)
    movie = response.json()
    a_movie = Movie(
        title=movie['title'],
        year=movie['release_date'][:4],
        description=movie['overview'],
        img_url=f"https://image.tmdb.org/t/p/w500{movie['poster_path']}",
    )
    db.session.add(a_movie)
    db.session.commit()
    find_movie_id = Movie.query.filter_by(title=movie['title']).first()
    return redirect(url_for('edit', movie_id=find_movie_id.id))


if __name__ == '__main__':
    app.run(debug=True)
