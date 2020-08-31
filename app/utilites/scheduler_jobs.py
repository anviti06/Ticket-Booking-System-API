from app.services.expiry_check import isActive 
from app.app import db
from app.models import User, Ticket

def markExpiredTickets():
    ticket_list = Ticket.query.all()
    for ticket in ticket_list:
        if not isActive(ticket.showTime):
            result = Ticket.query.filter_by(ticketId = ticket.ticketId).update(dict(isExpired = True))
            db.session.commit()
    return

    
def deleteExpiredTickets():
    ticket_list = Ticket.query.all()
    for ticket in ticket_list:
        if ticket.isExpired or not isActive(ticket.showTime):
            db.session.delete(ticket)
            db.session.commit()
    return
