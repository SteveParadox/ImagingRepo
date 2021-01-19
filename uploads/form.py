from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import FileField, StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired



class Register(FlaskForm):
    name = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField('Login')

class Store(FlaskForm):
    image = FileField('Image', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'])])
    name = StringField(validators=[DataRequired()])
    submit = SubmitField('Upload...')


