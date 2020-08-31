from flask import Flask,Blueprint,request,jsonify
from app.app import db
from app.models import Ticket,User
from sqlalchemy import update
from app.services.expiry_check import isActive
from app.services.ticket import book_ticket, update_time, delete_ticket
from app.services.view import view_user, view_ticket
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
		return book_ticket(data)
	return { 'result' : 'failure'}



"""
	Case 2: Update Ticket Timing
	
	Input: ticketId
	Output: success - updated
			failure - could not be updated / Ticket does not exist 
"""

@ticket_bp.route('/ticket/update/time' , methods = ['POST' , 'GET'])
def updateTime():
	if request.method =="POST":
		data = request.get_json()
		return update_time(data)

	return { 'result' : 'failure' }


"""
	Case 3: Delete Ticket
	
	Input: ticketId
	Output: success - Deleted
			failure - could not be deleted / Ticket does not exist 
"""
@ticket_bp.route('/ticket/delete' , methods = ['POST' , 'GET'])
def delete():

	if request.method =="POST":
		data = request.get_json()
		return delete_ticket(data)
	return { 'result' : 'failure' }



"""
	Case 4: Show all Tickets of a particulat time
	
	Input: showTime
	Output: success - All ticket details in json format
			failure - empty file 
"""
@ticket_bp.route('/ticket/view/time' , methods = ['POST' , 'GET'])
def view_time():

	if request.method =="POST":
		data = request.get_json()
		return view_ticket(data)
	return {'result': 'failure'}

"""
	Case 5: Show user Details of a particular ticket
	
	Input: ticketId
	Output: success - user details in json format
			failure - empty file 
"""

@ticket_bp.route('/ticket/view/user' , methods = ['POST' , 'GET'])
def user():

	if request.method =="POST":
		data = request.get_json()
		return view_user(data)	
	return {'result': 'failure'}




