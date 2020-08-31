"""Entry Point of the app"""
import os
from flask import Flask
from app.app import create_app,db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('dev') or 'test')

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run()


if __name__ == '__main__':
    manager.run()