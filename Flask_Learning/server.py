from flask import Flask
import random
app = Flask(__name__)

#Higher Or Lower Game

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
def game_intro():
    return '<h1>Guess a number between 0 and 9</h1> \
        <img src="https://media.giphy.com/media/13RcbHeXlLNysE/giphy.gif">'

@app.route('/<int:guess>')
def result(guess): 
    number = random.randint(0,9)
    if guess == number:
        return '<h1>You guessed the number!</h1> \
            <img src="https://media.giphy.com/media/PS7d4tm1Hq6Sk/giphy.gif"/>'
    elif guess > number:
        return '<h1>You guessed too high!</h1> \
            <img src="https://media.giphy.com/media/2cei8MJiL2OWga5XoC/giphy.gif"/>'
    else:
        return '<h1>You guessed too low!</h1> \
            <img src="https://media.giphy.com/media/ySsepgFviNzz8O8Yvj/giphy.gif"/>'



if __name__ == '__main__':
    app.run(debug=True)