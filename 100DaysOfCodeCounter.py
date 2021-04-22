#! /usr/bin/python3

from pathlib import Path
import datetime

# check for a special file
# if yes
#   read it: start_date
# else
#   ask user for start date
#   write start date to file
# calculate number of days since start date
# print

print("100 Days of Code Counter")

datapath = './startdate.data'
today = datetime.date.today()

p = Path(datapath)

if p.exists():
    with p.open('r') as f:
        start_date = datetime.datetime.strptime(f.readline(), "%Y-%m-%d").date()
else:
    print("Start Date not found.")
    userinput = input("Enter Start Date (YYYY-MM-DD), or [Enter] if today is your first day: \n")
    if userinput is '':
        start_date = datetime.date.today()
    else:
        start_date = datetime.datetime.strptime(userinput, "%Y-%m-%d").date()
    print("You have chosen ", start_date)

    print("Saving to startdate.data")
    with p.open('w') as f:
        f.write(start_date.strftime("%Y-%m-%d"))

delta = today - start_date

print("This is day %d of 100 Days of Code" % delta.days)
