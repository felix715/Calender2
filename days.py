import calendar
c = calendar.Calendar()
for day in c.itermonthdays(2021, 1):
    print(day)