from flask import (Flask, render_template, request,Blueprint)
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
#from apscheduler.schedulers.background import BackgroundScheduler

db = SQLAlchemy()
#scheduler = BackgroundScheduler(daemon=True)    


def create_app():
    
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    db.init_app(app)

    from .models import Ticket,User
    print(datetime.now())

    with app.app_context():
        """def check_price():
            with app.app_context():
                waitlist_table = Waitlist.query.all()
        
                for row in waitlist_table:
                    temp_product = Product.query.filter_by(pid = row.pid).first()
                    #print(temp_product.name)
                    if(temp_product.price <= row.threshold):
                        #print("Found product")
                        raise_notification(row.id , temp_product.pid)
                    #else:
                        #print("Not Found")
            return
            """

        from .ticket_api import ticket_bp as ticket_blueprint
        app.register_blueprint(ticket_blueprint)
        
        
        #Initializing Scheduler - event will occur every 5 seconds
        #scheduler.add_job(check_price, 'interval', seconds=5)          
        #scheduler.start()
        
        #db.create_all()
        return app
    