from flask import Flask,Blueprint,request,jsonify
from app.app import db
from app.models import Ticket,User
from sqlalchemy import update
from .expiry_check import isActive

def book_ticket(data):

    user_name = data['userName']
    phone_no = data['phoneNo']
    show_time = data['showTime']

	#Condition for Expiry : curTime - showTime < 8hr
    if not isActive(show_time):
        return {'result' : 'Enter valid Time'}
	#Checking Ticket count
    count = Ticket.query.filter_by(showTime = show_time).count()
    if count > 20:
        return { 'result' : 'Failure - Housefull!! More than 20 Tickets Exist!'} 
		
    user = User.query.filter_by(userName = user_name , phoneNo = phone_no).first()
    if not user:
        new_user = User(userName = user_name , phoneNo = phone_no)
        db.session.add(new_user)
        db.session.commit()
        user = User.query.filter_by(userName = user_name , phoneNo = phone_no).first()	
			

    new_entry = Ticket(userId = user.userId ,showTime = show_time)
    db.session.add(new_entry)
    db.session.commit()
		
    return { 'result' : 'Success - Ticket booked'}


def update_time(data):
    ticket_id = data['ticketId']
    show_time = data['showTime']
		
		#Checking Show time for expiry
    if(not isActive(show_time)):
        return {'result': 'Enter a Valid Time'}

    ticket = Ticket.query.filter_by(ticketId = ticket_id).first()
		
    if not ticket:
        return {'result' : 'Failure - No Ticket could be found!'}
		
    ticket = Ticket.query.filter_by(ticketId = ticket_id).update(dict(showTime = show_time))
    db.session.commit()
        
    return { 'result' : 'Success - Timings Updated'}

def delete_ticket(data):
    ticket_id = data['ticketId']
		
    ticket = Ticket.query.get(ticket_id)
		
    if not ticket:
        return {'result' : 'Failure - No Ticket could be found!'}
		
    db.session.delete(ticket)
    db.session.commit()
        
    return { 'result' : 'Success - Record Deleted'}