from flask import (Flask, render_template, request,Blueprint)
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


def create_app():
    
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    db.init_app(app)

    from .models import Ticket,User
    
    with app.app_context():

        from .ticket_api import ticket_bp as ticket_blueprint
        app.register_blueprint(ticket_blueprint)
        
        #db.create_all()
        return app
    