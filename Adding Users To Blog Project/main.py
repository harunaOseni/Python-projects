from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from forms import CreatePostForm, RegistrationForm, LoginForm, CommentForm
from flask_gravatar import Gravatar
from decouple import config
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.secret_key = config('SECRET_KEY')
login_manager = LoginManager()
login_manager.init_app(app)
gravatar = Gravatar(app, size=100, rating='g', default='retro',
                    force_default=False, force_lower=False)

# CONFIGURE TABLES


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    posts = db.relationship('BlogPost', backref='user')
    comments = db.relationship('Comment', backref='user')


db.create_all()


class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(
        db.Integer, db.ForeignKey('users.id'))
    author = db.Column(db.String(250))
    title = db.Column(db.String(250), unique=True)
    subtitle = db.Column(db.String(250))
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    comments = db.relationship('Comment', backref='blog_post')


db.create_all()


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(
        db.Integer, db.ForeignKey('users.id'))
    body = db.Column(db.Text)
    blog_post_id = db.Column(
        db.Integer, db.ForeignKey('blog_posts.id'))


db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


def admin_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.get_id() == "1":
            return func(*args, **kwargs)
        else:
            return abort(403)
    return wrapper


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    if posts:
        return render_template('index.html', all_posts=posts)
    else:
        return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    email = User.query.filter_by(email=form.email.data).first()
    if request.method == "POST":
        if form.validate_on_submit():
            if email:
                flash("You already have a blog house account, Log In", "success")
                return redirect(url_for('login'))
            else:
                username = form.username.data
                password = form.password.data
                confirm_password = form.confirm_password.data
                email = form.email.data
                hashed_password = generate_password_hash(
                    password, method='sha256')
                if password == confirm_password:
                    new_user = User(username=username, email=email,
                                    password=hashed_password)
                    db.session.add(new_user)
                    db.session.commit()
                    flash('You are now registered and can log in', 'success')
                    return redirect(url_for('login'))
                else:
                    flash('Passwords do not match', 'danger')
                    return redirect(url_for('register'))
    if request.method == "GET":
        return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('get_all_posts'))
            else:
                flash('Login Unsuccessful. Please check email and password', 'danger')
                return redirect(url_for('login'))
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route("/post/<int:post_id>", methods=['GET', 'POST'])
def show_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    blog_post = BlogPost.query.get(post_id)
    comments = blog_post.comments
    comment_form = CommentForm()
    if request.method == "POST":
        if comment_form.validate_on_submit():
            new_comment = Comment(
                body=comment_form.body.data,
                author_id=current_user.id,
                blog_post_id=post_id)
            db.session.add(new_comment)
            db.session.commit()
            return redirect(url_for('show_post', post_id=post_id))
    return render_template("post.html", post=requested_post, form=comment_form, comments=comments, gravatar=gravatar)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/new-post", methods=['GET', 'POST'])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_post = BlogPost(
                author_id=current_user.id,
                title=form.title.data,
                subtitle=form.subtitle.data,
                body=form.body.data,
                img_url=form.img_url.data,
                author=current_user.username,
                date=date.today().strftime("%B %d, %Y")
            )
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>", methods=['GET', 'POST'])
@admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if request.method == "POST":
        if edit_form.validate_on_submit():
            post.title = edit_form.title.data
            post.subtitle = edit_form.subtitle.data
            post.img_url = edit_form.img_url.data
            post.author = edit_form.author.data
            post.body = edit_form.body.data
            db.session.commit()
            return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form)


@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
