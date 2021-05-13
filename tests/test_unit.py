import unittest
from flask import url_for
from flask_testing import TestCase
from application import app, db, Register
from application.models import Games

class TestBase(TestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///data.db",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        db.create_all()
        db.session.add(Games(
                    game_name='Monopoly', 
                    age_rating=3,
                    genre='Board Game',
                    description='Destroys friendships'
                ) )
        db.session.add(Games(
                    game_name='Farming Simulator', 
                    age_rating=3,
                    genre='Simulation',
                    description='Pretend to be a farmer'
                ) )
        db.session.add(Games(
                    game_name='Doom', 
                    age_rating=18,
                    genre='First person shooter',
                    description='Shoot all the demons'
                ) )
        db.session.add(sample1)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()