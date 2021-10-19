from flask import Flask, render_template
import forms
from decouple import config
from flask import request
from flask_bootstrap import Bootstrap

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = config('SECRET_KEY')
    Bootstrap(app)
    return app

app = create_app()

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if request.method == 'GET':
        return render_template('login.html', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            if form.email.data == 'admin@email.com' and form.password.data == '12345678':
                return render_template('success.html')
            else:
                return render_template('denied.html')
        else:
            return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)