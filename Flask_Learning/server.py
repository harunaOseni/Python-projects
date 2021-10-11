from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"
    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        return "<em>" + function() + "</em>"
    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        return "<u>" + function() + "</u>"
    return wrapper_function


@app.route('/')  # A python decorator that tells flask what url to listen for
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return 'This is junior typing to the web from my nice room, how do you do?'


@app.route('/fuckoff')
def hello():
    return 'fuck off you\'re not supposed to be here'


@app.route('/<name>')
def hello_name(name):
    return f'<h1 style = {"text-align:center;"}>Hello {name}!</h1> \
        <p>You\'re a piece of shit, fuck you moron!</p> \
        <p> Bye Bitch! </p> \
        <img src="https://media.giphy.com/media/YorwDAH66ln3O/giphy.gif" />'


if __name__ == '__main__':
    app.run(debug=True)
