from flask_testing import TestCase

from .app import db
from main import app


class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object(".app.config.TestingConfig")
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()