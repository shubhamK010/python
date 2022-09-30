# # delta = change 
# # to get difference between dates 




# SOLUTION 
import datetime

t1= datetime.datetime.today() # we are using only date method from datetime module
t2 = datetime.datetime(2023,2,15) # focus on the year , use next year if the bday is already celebrated for the year
Hbday_in = t2 - t1
print(Hbday_in)
print(Hbday_in.days) # to get only days in output use 'days' method


# Daylight saving time(DST)=Daylight saving time, also known as daylight savings time or daylight time, 
# and summer time, is the practice of advancing clocks during warmer months 
# so that darkness falls at a later clock time

# Coordinated Universal Time(UTC)=Coordinated Universal Time or UTC is the primary time standard 
# by which the world regulates clocks and time.It is effectively a successor to Greenwich Mean Time.

# Greenwich Mean Time Zone(GMT)=Greenwich Mean Time (GMT) has been used to clearly designate epoch 
# by avoiding confusing references to local time systems (zones). 
# Historically, astronomers used Greenwich Mean Astronomical Time (GMAT), 
# in which the astronomical day began at noon at longitude (0°), in accord with scientific tradition.
# If you're west of the Prime Meridian, your GMT will be ahead of, or minus, the time at the Prime Meridian.



















# from datetime import datetime
# from datetime import timedelta
# today = datetime.today()
# birthday = today - timedelta(days=150)
# print(today)
# print()
# print(birthday)