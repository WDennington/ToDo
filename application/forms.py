from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    description = StringField('Description of the Task', validators=[DataRequired()])
    submit = SubmitField('Add Task')