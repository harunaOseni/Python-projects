from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


db.create_all()

@app.route('/')
def home():
    read_book = Book.query.all()
    return render_template('index.html', books=read_book)


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        rating = request.form['rating']
        entry = Book(title=title, author=author, rating=rating)
        db.session.add(entry)
        db.session.commit()
        read_books = Book.query.all()
        return redirect(url_for('home', books=read_books))
    else:
        return render_template('add.html')


@app.route("/edit/<int:book_id>", methods=['POST', 'GET'])
def edit(book_id):
    book = Book.query.get(book_id)
    if request.method == 'POST':
        book.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('edit.html', book=book)


@app.route("/delete/<int:book_id>")
def delete(book_id):
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home', books=Book.query.all()))

if __name__ == "__main__":
    app.run(debug=True)