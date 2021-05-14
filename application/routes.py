from flask import Flask, render_template, request, redirect, url_for
from application.forms import AddGame, AddRating
from application import app, db
from application.models import GameRatings, Games


@app.route('/')
@app.route('/home')
def home():
    all_games = Games.query.all()
    all_ratings = GameRatings.query.all()
    output = ''
    return render_template("index.html", title="Home", all_games=all_games, all_ratings=all_ratings)
    

@app.route('/add_game', methods=["GET","POST"])
def add_game():
    form = AddGame()
    if request.method == "POST":
        if form.validate_on_submit():
                new_game = Games(
                    game_name=form.game_name.data, 
                    age_rating=form.age_rating.data,
                    genre=form.genre.data,
                    description=form.description.data
                )           
                db.session.add(new_game)
                db.session.commit()
                return redirect(url_for("home"))

    return render_template("add.html", title="Add a Game", form=form)

@app.route('/update/<int:game_id>', methods=["GET", "POST"])
def update(game_id):
    form = AddGame()
    update = Games.query.get(game_id)
    if form.validate_on_submit():
        update.game_name = form.game_name.data
        update.age_rating = form.age_rating.data
        update.genre = form.genre.data
        update.description = form.description.data
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template('update.html', title = 'Update Game Info', form=form, update=update)


@app.route('/add_rating', methods=["GET","POST"])
def add_rating():
    form = AddRating()
    if request.method == "POST":
        if form.validate_on_submit():
            game = Games.query.filter_by(game_name=form.game_name.data).first()
            new_rating = GameRatings(rating=form.rating.data)
            new_rating.game = game

            db.session.add(new_rating)
            db.session.commit()
            if GameRatings(rating=form.rating.data) is not None:
                rated1 = Games.query.filter_by(game_name=form.game_name.data).first()
                rated1.rated = True
                db.session.commit()
            return redirect(url_for("home"))

    return render_template("rating.html", title="Add a Rating", form=form)

@app.route('/delete_game/<int:game_id>', methods=["POST", "GET"])
def delete_game(game_id):
    delete = Games.query.filter_by(game_id=game_id).first()
    db.session.delete(delete)
    db.session.commit()
    return redirect(url_for("home"))
    
