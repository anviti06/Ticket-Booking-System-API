import datetime
import json
import unittest
from urllib import parse

from app.app.models import Ticket,User
from .BaseCase import BaseTestCase

dummy_userName = "Ajay"
dummy_phoneNo = "9877699008"
dummy_showTime = "2020-08-31 12:00:00.0000"
dummy_invalid_showTime = "2020-08-30 12:00:00.0000"




def book_ticket(self, name, number, showTime):
    return self.client.post(
        "/ticket/book",
        data=json.dumps(
            dict(
                userName=name,
                phoneNo=number,
                showTime = showTime
            )
        ),
        content_type="application/json",
    )




"""Sapmle Test Cases """
class TestTicketBook(BaseTestCase):

    def test_book_ticket(self):
        with self.client:

            response = book_ticket(self, dummy_userName, dummy_phoneNo, dummy_showTime)
            response_json = response.json
            self.assertEqual(response_json['result'], 'Success - Ticket booked')
    
    def check_ticket_time(self):
        response = book_ticket(self, dummy_userName, dummy_phoneNo, dummy_invalid_showTime)
        response_json = response.json
        self.assertEqual(response_json['result'], 'Success - Ticket booked')
    
