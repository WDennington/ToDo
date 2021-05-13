from application import db

class Games(db.Model):  
    game_id = db.Column(db.Integer, primary_key=True)
    game_name = db.Column(db.String(80), nullable=False)
    age_rating = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(40))
    description = db.Column(db.String(200))
    rated = db.Column(db.Boolean, nullable=False, default=False)
    ratings = db.relationship('GameRatings', backref='game')

class GameRatings(db.Model):
    rating_id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey('games.game_id'), nullable=False)
