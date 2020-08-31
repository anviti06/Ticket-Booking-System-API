from flask import (Flask, render_template, request,Blueprint)
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from .config import config_type
from apscheduler.schedulers.background import BackgroundScheduler


db = SQLAlchemy()

def create_app(config_name):
    
    app = Flask(__name__)
    app.config.from_object(config_type[config_name])
    db.init_app(app)

    with app.app_context():
        #Registering Blueprints
        from .controller.ticket_api import ticket_bp as ticket_blueprint
        app.register_blueprint(ticket_blueprint)
        
        #Initializing Scheduler - checking for expiry every hour and deleting them every 8 hours
        scheduler = BackgroundScheduler(daemon=True)
        from .utilites.scheduler_jobs import markExpiredTickets, deleteExpiredTickets
        scheduler.add_job(markExpiredTickets, 'interval', seconds = 60*60)    #Every Hour          
        scheduler.add_job(deleteExpiredTickets, 'interval', seconds= 8*60*60)    #Evry 8 hour           
        scheduler.start()
        

        #db.create_all()
        return app



