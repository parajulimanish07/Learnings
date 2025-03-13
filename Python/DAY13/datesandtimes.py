import datetime

date = datetime.date(2025, 2,27)
today = datetime.date.today() #this is the current date

time = datetime.time(12, 30, 0)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %m-%d-%Y")


target_datetime = datetime.datetime(2020, 2, 28, 12, 30, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime :
    print("The target date has already passed.")
else:
    print("The target date has not passed yet.")