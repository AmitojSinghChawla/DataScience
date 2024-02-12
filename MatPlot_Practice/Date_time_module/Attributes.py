import datetime
import pytz
# #datetime.date usages
#
# d=datetime.date(2023,12,3)
# print(d)
# #prints a date
#
# print(datetime.date.today())
# #prints today's date
#
# # Time delta is a value which we get when we perform an operation(mathematical on 2 dates)-->
# # eg date1-date2=time delta
# # eg date1+date2= time delta
#
# #Time Delta Examples
#
# tday=datetime.date.today()
# bday=datetime.date(2024,3,15)
# #my birth date
#
# ab=bday-tday #gives us 32 as of today
# print(ab.days) #prints total days left
# print(ab.total_seconds()) #prints total seconds left
#
#
# #2.  (datetime.time attribute)
#
# t=datetime.time(9,35,29,300000)
# print(t)
# print(t.hour)
#
# # 3 datetime.datetime
#
# dt=datetime.datetime(2024,3,24,12,20,45,100)
#
# print(dt)
# print(dt.time())
# print(dt.day)
#
# tdelta=datetime.timedelta(hours=12)
#
# print(dt+tdelta)
#
# #timezone aware time
# # You install python library as recommended by the documentation itself that pytz library for timezone aware date time

dt_now=datetime.datetime.now(tz=pytz.UTC)
print(dt_now) # this is a timezone aware date time which was made so by using the pytz library


dt_india=dt_now.astimezone(pytz.timezone("Asia/Kolkata"))
print(dt_india) # in this we have made aware the datetime to my current area timezone


dt_now1=datetime.datetime.now()
print(dt_now1) # this is also called as a nive datetime as it just picks the local time from my computer without any information about the UTC timezone

#you can make a naive date time ware about timezone like down below or directly call this method---> dt_india=dt_now.astimezone(pytz.timezone("Asia/Kolkata"))

indian_time=pytz.timezone("Asia/Kolkata")
dt_now1=indian_time.localize(dt_now1)


