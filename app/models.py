from .app import db

class User(db.Model):
    __tablename__ = 'user_record'
    userId = db.Column(db.Integer, primary_key=True, unique = True)
    userName = db.Column(db.String(60))
    phoneNo = db.Column(db.String(60))
    

class Ticket(db.Model):
    __tablename__ = 'ticket_record'
    ticketId = db.Column(db.Integer, primary_key=True , unique = True)
    userId = db.Column(db.Integer)
    showTime = db.Column(db.String(20))
    isExpired = db.Column(db.Boolean , default=False)
    


