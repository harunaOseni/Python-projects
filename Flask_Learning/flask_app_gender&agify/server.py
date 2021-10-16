from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__, template_folder=r'C:\Users\oseni haruna\OneDrive\Documents\Python Programming\Day57\Dynamic Blog Project\template')


@app.route('/')
def homepage():
    # get the current year
    now = datetime.now()
    year = now.year
    return render_template('index.html', current_year=year)


@app.route('/guess/<string:user_name>')
def guess(user_name):
    # using the ageify api
    parameter = {'name': user_name}
    response = requests.get(url="https://api.agify.io/", params=parameter)
    user_age_json = response.json()
    user_age = user_age_json['age']

    # using the genderize api
    parameter = {"name": user_name}
    response02 = requests.get(
        url="https://api.genderize.io/", params=parameter)
    user_gender_json = response02.json()
    user_gender = user_gender_json["gender"]
    user_probability = user_gender_json["probability"]

    return render_template('index.html', user_name=user_name, user_age=user_age, 
    user_gender = user_gender, user_probability = user_probability)


if __name__ == '__main__':
    app.run(debug=True)
