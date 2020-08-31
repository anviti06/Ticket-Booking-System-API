import os
import unittest
from flask import current_app
from flask_testing import TestCase,unittest
from main import app


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object("config.DevelopmentConfig")
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config["DEBUG"] == True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config["SQLALCHEMY_DATABASE_URI"]== "sqlite:///MovieTicketDatabase")
        )


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object("config.TestingConfig")
        return app

    def test_app_is_testing(self):
        self.assertTrue(app.config["DEBUG"])
        self.assertTrue(
            app.config["SQLALCHEMY_DATABASE_URI"]== "sqlite:///Test_MovieTicketDatabase" )
        )


if __name__ == "__main__":
    unittest.main()