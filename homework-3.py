# Author: Jonathan Habashey
# Date: 02/10/2020
# Filename: homework-3.py
# Description: Uses date and time functions like time, datetime, and calendar functions
from datetime import date
from datetime import datetime
import calendar
import time


today_date = date.today()
print(today_date)

today_date_string = today_date
print(today_date_string.strftime("%m-%d-%Y"))

graduation = "May 15, 2020"
datetime.strptime(graduation, '%B' + ' ' + '%d, ' + '%Y')




today_weekday = today_date.weekday()

if today_weekday == 0:
    print("Monday")
if today_weekday == 1:
    print("Tuesday")
if today_weekday == 2:
    print("Wednesday")
if today_weekday == 3:
    print("Thursday")
if today_weekday == 4:
    print("Friday")
if today_weekday == 5:
    print("Saturday")
if today_weekday == 6:
    print("Sunday")