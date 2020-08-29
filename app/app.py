from flask import (Flask, render_template, request,Blueprint)
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

db = SQLAlchemy()
scheduler = BackgroundScheduler(daemon=True)    


def create_app():
    
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    db.init_app(app)

    #Importing Databse Models
    from .models import Ticket

    with app.app_context():
        #Desiging the scheduler function 
        from .utilites import isActive 
        def deleteExpiredTickets():
            with app.app_context():
                ticket_list = Ticket.query.all()
                for ticket in ticket_list:
                    if ticket.isExpired or not isActive(ticket.showTime):
                        db.session.delete(ticket)
                        db.session.commit()
            return


        #Registering Blueprints
        from .ticket_api import ticket_bp as ticket_blueprint
        app.register_blueprint(ticket_blueprint)
        
        #Initializing Scheduler - marking of tickets as expired will occur every 5 seconds
        scheduler.add_job(deleteExpiredTickets, 'interval', seconds=5)          
        scheduler.start()
        

        #db.create_all()
        return app
    