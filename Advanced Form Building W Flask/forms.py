from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length
import email_validator


class LoginForm(FlaskForm):
    email = StringField(label='email', validators=[
                        DataRequired(), Email(message="Please enter a correct email")])
    password = PasswordField(label='password', validators=[
                             DataRequired(),  Length(min=8)])
    submit = SubmitField(label='Login')
