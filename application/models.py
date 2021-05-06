from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(1000))


class TaskEntry(FlaskForm):
    task_name = StringField("Task Name:")
    task_description = StringField("Short Task Description")
    task_complete = BooleanField() 