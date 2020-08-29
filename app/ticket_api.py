from flask import Flask,Blueprint,request,jsonify
from .app import db
from .models import Ticket,User
from sqlalchemy import update
import datetime
from datetime import timedelta
		
ticket_bp = Blueprint('ticket_bp', __name__)



"""
	Case 1: Book Ticket
	
	Input: user name, phone number, timings
	Output: success - ticket added in database
			failure - ticket could not be added 
"""

@ticket_bp.route('/ticket/book' , methods = ['POST' , 'GET'])
def book_new():

	if request.method =="POST":
		
		data = request.get_json()
		user_name = data['userName']
		phone_no = data['phoneNo']
		show_time = data['showTime']

		
		#Checking Ticket count
		count = Ticket.query.filter_by(showTime = show_time).count()
		if count > 20:
			return { 'result' : 'Failure - Housefull!! More than 20 Tickets Exist!'} 
		
		user = User.query.filter_by(userName = user_name , phoneNo = phone_no).first()
		
		#Checking entry in User Table
		if not user:
			new_user = User(userName = user_name , phoneNo = phone_no)
			db.session.add(new_user)
			db.session.commit()
			user = User.query.filter_by(userName = user_name , phoneNo = phone_no).first()	


		new_entry = Ticket(userId = user.userId ,showTime = show_time)
		db.session.add(new_entry)
		db.session.commit()
		
		return { 'result' : 'Success - Ticket booked'}

	return { 'result' : 'failure'}
		




"""
	Case 2: Update Ticket Timing
	
	Input: ticketId
	Output: success - updated
			failure - could not be updated / Ticket does not exist 
"""
@ticket_bp.route('/ticket/update/time' , methods = ['POST' , 'GET'])
def update_time():
	if request.method =="POST":

		data = request.get_json()
		ticket_id = data['ticketId']
		show_time = data['showTime']

		ticket = Ticket.query.filter_by(ticketId = ticket_id).first()
		
		if not ticket:
			return {'result' : 'Failure - No Ticket could be found!'}
		
		ticket = Ticket.query.filter_by(ticketId = ticket_id).update(dict(showTime = show_time))
		db.session.commit()
        
		return { 'result' : 'Success - Timings Updated'}

	return { 'result' : 'failure' }




"""
	Case 3: Delete Ticket
	
	Input: ticketId
	Output: success - Deleted
			failure - could not be deleted / Ticket does not exist 
"""
@ticket_bp.route('/ticket/delete' , methods = ['POST' , 'GET'])
def delete_ticket():

	if request.method =="POST":
		data = request.get_json()
		ticket_id = data['ticketId']
		
		ticket = Ticket.query.get(ticket_id)
		
		if not ticket:
			return {'result' : 'Failure - No Ticket could be found!'}
		
		db.session.delete(ticket)
		db.session.commit()
        
		return { 'result' : 'Success - Record Deleted'}

	return { 'result' : 'failure' }


