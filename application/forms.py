from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, HiddenField, IntegerField, FloatField, SelectField
from wtforms.validators import DataRequired

class AddRating(FlaskForm):
    game_name = StringField('Game name')
    rating = FloatField('Rating out of 10')
    submit = SubmitField('Add Rating')

class AddGame(FlaskForm):
    game_id= HiddenField()
    game_name = StringField('Game name')
    age_rating = SelectField('Rating:',
        choices=[
        ('3', '3+'),
        ('7', '7+'),
        ('12', '12+'),
        ('18', '18+')
        ])
    genre = StringField('Genre')
    description = StringField('Short description of the game')
    submit = SubmitField('Add/Update Game')   

class DeleteGame(FlaskForm):
    game_to_delete = StringField('Game name')
    submit = SubmitField('Delete Game')