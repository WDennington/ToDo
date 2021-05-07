from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField
from datetime import datetime

class Tasks(db.Model):  
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(1000), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    date_created = db.Column(db.DateTime,nullable=False, default=datetime.utcnow)


class TaskEntry(FlaskForm):
    task_name = StringField("Task Name:")
    task_description = StringField("Short Task Description")
    task_complete = BooleanField() 