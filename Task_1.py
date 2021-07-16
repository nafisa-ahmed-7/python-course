#Get a birthday
from datetime import date
def calculateAge(birthDate):
    days_in_year = 365
    age = int((date.today() - birthDate).days / days_in_year)
    return age
print(calculateAge(date(1998, 2, 22)), "years")

#find the day of the week
import datetime
import calendar


def Day(date):
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[born])
date = '22 02 1998'
print(Day(date))