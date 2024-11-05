from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class EditForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    currentpassword = PasswordField('Current Password', validators=[DataRequired()])
    newpassword = PasswordField('New Password', validators=[DataRequired()])
    submit = SubmitField('Edit')

class DeleteForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Delete')