from flask import Flask,Blueprint,request,jsonify
from app.app import db
from app.models import Ticket,User
from sqlalchemy import update
from .expiry_check import isActive

def view_user(data):
    ticket_id = data['ticketId']
    ticket = Ticket.query.filter_by(ticketId = ticket_id).first()
		
    if not ticket or ticket.isExpired:
        return {'result' : 'Failure-Ticket could not be found'}
		
    user = User.query.filter_by(userId = ticket.userId).first()
    dict = {'userName' : user.userName ,'phoneNo': user.phoneNo}
    return dict

    
def view_ticket(data):
    show_time = data['showTime']

    data = []
    ticket_list = Ticket.query.filter_by(showTime = show_time)
		
    for ticket in ticket_list:
        user = User.query.filter_by(userId = ticket.userId).first()
        dict = {'ticketId' : ticket.ticketId , 'userName' : user.userName, 'phoneNo': user.phoneNo, 'showTime': ticket.showTime, 'isExpired': ticket.isExpired}
        data.append(dict)
    return jsonify(data)    