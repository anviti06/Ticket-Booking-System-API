from app.app import db
from app.models import Ticket,User
from datetime import datetime, timedelta

"""
	Function to find the difference current time and given time
"""
def isActive(time):
	#Converting strings to dates
	datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
	date = datetime.strptime(time, datetimeFormat)
	dif = datetime.now()-date
	ans = divmod(dif.total_seconds(), 60)
	if ans[0]<480 :		#480 minutes = 8hours
		return True
	return False