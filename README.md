<h1 align = center> Ticket Booking System </h1>

<h4 align = center>A REST interface for ticket booking system</h4>
The interface follows REST paradigm with <b>Python + Flask</B> as the HTTP server and router, and <b>MySQL</b>server for the database. All requests from the front end are served by a Python server running Flask as the application framework. MySQL's Python connector is used to query the MySQL server, which executes the queries on a relational database.

The system is built to serve as an onsite ticket booking system for a movie theatre. 
All HTTP requests to Flask are made via encrypted POST messages. The system is designed to be secure, robust and flexible. The requirements mandated the use of a stored procedure and a trigger in MySQL.
 

 ---
 <br>
  
## Dependencies
**Flask** Python HTTP router

**MySQL** Database server

 <br> 
 
 ---
 
 <br>
 
## Functionalities

<br>

### Endpoints:

 1.  [`/ticket/book`](https://github.com/anviti06/Ticket-Booking-System-API/blob/6948880b306921d83c43011cef80f0cae1b2138a/app/ticket_api.py#L19):  
	 - ***Input:** User's Name, Phone Number, Ticket Show time*
	 -  The UserId of particular User is fetched using the userName & phoneNo in the user_record table (If user does not exists then it is first added in record and then userId is fetched).
	 - New Record is made in ticket_record table using the userId, showTime, isExpired(default = false) fields with respective values.
	 - **Conditions Checked:** 
		 - expiry limit of showTime given as input
		 - count of already booked ticket for particular showTime is not more than 20.  
		 
 2. [`/ticket/update/time`](https://github.com/anviti06/Ticket-Booking-System-API/blob/6948880b306921d83c43011cef80f0cae1b2138a/app/ticket_api.py#L66):
	 - ***Input:** Ticket Id, new Show Time to be updated*
	 -  Ticket entity is fetched using the ticketId from ticket_record and then the the showTime is updated with the new time.
	 - **Conditions Checked:** 
		 - expiry limit of showTime entered by user before inserting into table.
		 - ticket to be updated exists in table.  
	 
 3. [`/ticket/delete`](https://github.com/anviti06/Ticket-Booking-System-API/blob/6948880b306921d83c43011cef80f0cae1b2138a/app/ticket_api.py#L100):
	 - ***Input:** Ticket Id*
	 -  Ticket entity is fetched using the ticketId from ticket_record and delete operation is performed for that ticket.
	 - **Conditions Checked:** 
		 - expiry limit of showTime entered by user before inserting into table.
		 - ticket to be updated exists in table.  
 4. [`/ticket/view/time`](https://github.com/anviti06/Ticket-Booking-System-API/blob/6948880b306921d83c43011cef80f0cae1b2138a/app/ticket_api.py#L129):
	 - ***Input:** Show Time*
	 -  For each entity in ticket_record having showTime same as input, the userId from ticket_record table is use to fetch corresponding user details. 
	 - All these fetched entities are returned in json format.   

 5. [`/ticket/view/user`](https://github.com/anviti06/Ticket-Booking-System-API/blob/6948880b306921d83c43011cef80f0cae1b2138a/app/ticket_api.py#L161):
 	 - ***Input:** Ticket Id*
	 -  For the particular ticketId, the corresponding userId is used to fetch user's detail form user_record table.
	 - The details are returned in json format.  
	 - **Conditions Checked:** 
		 - Entity exists for given ticketId.
		 - Entity corresponding to given ticketId is not expired.  

<br>

### Checking Expiry of Tickets:
*Function implemented:* [isActive()](https://github.com/anviti06/Ticket-Booking-System-API/blob/f45f4bcff13880654fd9167c0bdd28c2534f675d/app/utilites.py#L8) 
- All tickets in which the Show Time is eight or more hours before the current time are considered to be expired.

<br><br>

### Scheduler Design:
*Function Implemented:* [deleteExpiredTickets()](https://github.com/anviti06/Ticket-Booking-System-API/blob/f45f4bcff13880654fd9167c0bdd28c2534f675d/app/app.py#L22)
- **Background scheduler** from **[APScheduler library](https://apscheduler.readthedocs.io/en/stable/userguide.html)** in Flask is used.
- The scheduler checks all entities of ticket_record table for the expiry of tickets(based on time difference of current time & show time) and marks those entites as expiried. **It then also deletes those entities from table.**


