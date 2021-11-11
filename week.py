import calendar
c = calendar.Calendar()
for week in c.monthdayscalendar(2020, 12):
    print(week)