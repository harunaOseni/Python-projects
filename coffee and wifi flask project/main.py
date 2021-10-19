from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import URL, DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    cafe_location = StringField(
        'Cafe location on Google Maps (URL)', validators=[DataRequired(message="Invalid Data"), URL(message='This is not a valid URl, please try again.')])
    opening_times = StringField(
        'Opening Time e.g. 8AM', validators=[DataRequired()])
    closing_times = StringField(
        'Closing Time e.g. 5:30PM', validators=[DataRequired()])
    coffee_rating = SelectField(label='Coffee Rating', choices=[
                                '☕', '☕,☕', '☕,☕,☕', '☕,☕,☕,☕', '☕,☕,☕,☕,☕'])
    wifi_strength_rating = SelectField(label='WiFi Strength Rating', choices=['✘',
                                                                              '💪', '💪,💪', '💪,💪,💪', '💪,💪,💪,💪', '💪,💪,💪,💪,💪'])
    power_socket_availability = SelectField(label='Power Socket Availability', choices=[
        '✘', '🔌', '🔌,🔌', '🔌,🔌,🔌', '🔌,🔌,🔌,🔌', '🔌,🔌,🔌,🔌,🔌'])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    # then write the form data into the csv file in new line
        #then redirect to cafes.html
        with open(file='cafe-data.csv', mode='a', encoding='utf8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([form.cafe.data, form.cafe_location.data, form.opening_times.data, form.closing_times.data, form.coffee_rating.data, form.wifi_strength_rating.data, form.power_socket_availability.data])
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form) 


@app.route('/cafes')
def cafes():
    with open(file='cafe-data.csv', mode='r', newline='', encoding='utf8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        lengthOfList = len(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows, length=lengthOfList)


if __name__ == '__main__':
    app.run(debug=True)
