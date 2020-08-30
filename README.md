<h1 align = center> Ticket Booking Manager</h1>
<h5 align = center>A REST interface for ticket booking system</h5>
The interface follows REST paradigm with <b>Python + Flask</B> as the HTTP server and router, and <b>MySQL</b>server for the database. All requests from the front end are served by a Python server running Flask as the application framework. MySQL's Python connector is used to query the MySQL server, which executes the queries on a relational database.

The system is built to serve as a ticket booking system for a movie theatre. It manages and handles all ticket related queries such as :
<ul>
<li>	Booking tickets for a show time.
<li>	Updating timings of already booked tickets
<li>	Deleting tickets from database
<li>   	View Ticket details using filters like specific show time
<li>	View User details for a ticket
<li>	Maintaining  Max ticket count for a show time
<li>	Checking expiry limit of all booked tickets in regular intervals and deleting expired ones from database. 
</ul>  
 
 <br>
 
 <br>
  
## Dependencies
**Flask** Python HTTP router

**MySQL** Database server

<br>
<br>

  
 ##  Entity Relationship Diagram
 <div align="center">
	
 <img src="https://i.ibb.co/MSkpsYG/Untitled-drawing.png" alt="Untitled-drawing" border="0">

</div>
 
 <br>
 <br>
 
 ## Database Schema
 <div align="center">

<img src="https://i.ibb.co/2sQz2TB/Untitled-drawing2.png" alt="Untitled-drawing2" border="0">

<div>

## How to run ?
1. #### Go to the project repository and download the requirements file 
		pip install -r requirements.txt
2. #### Running the Flask app - Go to the terminal of the root project directory and type:
		python main.py

	##### For testing, requests can be send through POSTMAN software and corresponding output can be visualized.

<br>

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

		<br>
		<div align="center">
		
		<img src="https://i.ibb.co/580Tstr/1.png" alt="Ticket Booking" border="0" title = " Ticket Booking" >
		
		<h6 align = center >Booking New ticket</h6>
		</div>

		<br>
		

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
		 
		
		

<br>

 4. [`/ticket/view/time`](https://github.com/anviti06/Ticket-Booking-System-API/blob/6948880b306921d83c43011cef80f0cae1b2138a/app/ticket_api.py#L129):
	 - ***Input:** Show Time*
	 -  For each entity in ticket_record having showTime same as input, the userId from ticket_record table is use to fetch corresponding user details. 
	 - All these fetched entities are returned in json format.   

		<div align = "center">
		
		<img src="https://i.ibb.co/S7P9bMC/6.png" alt="6" border="0">
		
		
		 <h6 align = center>Display list of all tickets of particular time</h6>
		
		</div>

<br>


 5. [`/ticket/view/user`](https://github.com/anviti06/Ticket-Booking-System-API/blob/6948880b306921d83c43011cef80f0cae1b2138a/app/ticket_api.py#L161):
 	 - ***Input:** Ticket Id*
	 -  For the particular ticketId, the corresponding userId is used to fetch user's detail form user_record table.
	 - The details are returned in json format.  
	 - **Conditions Checked:** 
		 - Entity exists for given ticketId.
		 - Entity corresponding to given ticketId is not expired.  
		 
		 <div align="center">
		 
		 <img src="https://i.ibb.co/mNrgfSs/user.png" alt="user" border="0">
		 
		 <h5> Displaying User Details of a particular ticket</h5>
		 
		 </div>

<br>

### Checking Expiry of Tickets:
*Function implemented:* [isActive()](https://github.com/anviti06/Ticket-Booking-System-API/blob/f45f4bcff13880654fd9167c0bdd28c2534f675d/app/utilites.py#L8) 
- All tickets in which the Show Time is eight or more hours before the current time are considered to be expired.
	
	<div align = "center" >
	
	<img src="https://i.ibb.co/54pGkSW/4.png" alt="Checking Expiry" border="0">
	
	</div>
<br>

### Scheduler Design:
*Function Implemented:* [deleteExpiredTickets()](https://github.com/anviti06/Ticket-Booking-System-API/blob/f45f4bcff13880654fd9167c0bdd28c2534f675d/app/app.py#L22)
- **Background scheduler** from **[APScheduler library](https://apscheduler.readthedocs.io/en/stable/userguide.html)** in Flask is used.
- The scheduler checks all entities of ticket_record table for the expiry of tickets(based on time difference of current time & show time) and marks those entites as expiried. **It then also deletes those entities from table.**

<br>

<br>
