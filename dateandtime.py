#Wrap my head around date and time
#relevant module is datetime
import datetime

#the datetime module contains different classes, one of these is the datetime class. 

#DATETIME CLASS
#Attributes of the datetime class are: year, month, day, hour, minute, second, microsecond and tzinfo (time zone info).
#We use the datetimeclass with the now() method to create a datetime obbject and the attributes set to the current date and time.
# the timezone info is populated as None with the now() method if no timezone argument is passed to it. 

#get current date and time
right_now = datetime.datetime.now()
print(f"\nUsing now() with datetime class:\ndatetime.datetime.now()   = {right_now} with data type {type(right_now)}")
print(f"Using today() with datetime class:\ndatetime.datetime.today() = {datetime.datetime.today()} with data type {type(datetime.datetime.today())}")

#DATE CLASS
#Creates objects with the date only, not time. 
#Attributes of the date class: year, month, day
#date class creates "idealized naive dates" (from Python documentation). This means no timezone awareness.
#use the today() method to populate with today's date (and time - if used on datetime class!). 
todays_date = datetime.date.today()
print(f"Using today() with date class:\ndatetime.date.today()     = {todays_date} with data type {type(todays_date)}")
print("Using now() with with the date class would return an error because it passes in an argument for timezone (set to None as default) which date classs does not expect.")

#DIFFERENCE BETWEEN NOW() AND TODAY()
#now() takes tzinfo as an argument whereas today() doesn't take any arguments. 
#Default argument for tzinfo is tz=None.
#Using now() with the date class will result in an error because it passes in an argument for timezone which date does not expect.")

#OTHER DATETIME MODULE CLASSES
# datetime.time (attributes are hour, minute, second, microsecond, tzinfo)
# datetime.timedelta (a duration that represents the difference between two date, datetime or time objects)
# datetime.tzinfo (used by the datetime and time classes to provide timezone information)
# datetime.timezone (shows the tzinfo as an offset from UTC)
