import pytz
import datetime


indian_time=datetime.datetime.now(tz=pytz.timezone("Asia/Kolkata"))

print(indian_time.strftime('%B %d %Y'))
# '%B %d %Y you can find more format in the python documentation to print date time as you like
#please refer to the documentaion for it

#--> this is the output February 12 2024

#strftime converts a datetime to a string
#strptime converts a string to date time

dt_time= 'march 15 2003'
dt=datetime.datetime.strptime(dt_time,'%B %d %Y')
print(dt)