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

#CREATING DATE OBJECTS
a_date = datetime.date(2023,6,2)
#date() is a constructor of the date class.
print(f"datetime.date(2023,6,2)     = {a_date}")
print(f"datetime.datetime(2023,6,2) = {datetime.datetime(2023,6,2)}")
print(f"a_date.year = {a_date.year}")
print(f"a_date.month = {a_date.month}")
print(f"a_date.day = {a_date.day}")
#If we want to import only the date class from the datetime module we could write
#from datetime import date
#and then we could write a_date = date(2023,6,2)

#FORMATTING DATETIME
#strftime() method creates a formatted string from a given date, datetime or time object
#i.e. the method is defined for the classes date, datetime, time
print(f"right_now.strftime('%D %d %M %Y, %H:%M:%S') = {right_now.strftime('%d/%m/%Y, %H:%M:%S')}")
# strptime() method creates a datetime object from a given string format, i.e. goes the other way around to strftime() 
#strptime() takes two arguments: striptime(string representing date and time, formatting mask)

#Example converting an ISO date string into an easily readable format

date = "2021-07-03T07:00:00+08:00"
print("Starting with a string 2021-07-03T07:00:00+08:00")
dt_1 = datetime.datetime.strptime(date,"%Y-%m-%dT%H:%M:%S%z")
print(f"datetime.strptime(date,'%Y-%m-%dT%H:%M:%S%z') = {dt_1}")
print(f"And then dt_1 = dt_1.strftime('%A %d %b %Y') = {dt_1.strftime('%A %d %b %Y')}")

# FORMATS
# %a Abbreviated weekday Sun, Mon, Tue
# %A full weekday name Sunday, Monday, Tuesday
# %w weekday as a decimal number 0,1,2,3,4,5,6
# %d day of month (zero padded decimal)
# %-d day of month NOT zero padded
# %b abbbreviated month name
# %B full month name
# %m month zero padded decimal
# %-m month decimal NOT zero padded
# %y year without century
# %Y full year
# %H, %-H hour, 24H
# %I, %-I hour, 12H
# %p AM or PM
# %M, %-M, %S, %-S
# %f microsecond
# %z UTC offset
# %Z timezone name
# %j, %-j day of the year
# %U week number of the year (Sunday start)
# %W week number of the year (Monday start)
# %c locale's date and time
# %x locale's date
# %X locale's time