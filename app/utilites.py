from .app import db
from .models import Ticket,User
from datetime import datetime, timedelta

def isActive(time):
	#Converting strings to dates
	datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
	date = datetime.strptime(time, datetimeFormat)
	dif = datetime.now()-date
	#print(dif.seconds)
	ans = divmod(dif.total_seconds(), 60)
	if ans[0]<480:
		return True
	return False