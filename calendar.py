import calendar

print(calendar.weekheader(3))

print()

print(calendar.firstweekday())

print()

print(calendar.month(2019,10))

print(calendar.monthcalendar(2019,10))

print()

print(calendar.calendar(2019))
day_of_the_week = calendar.weekday(2019,10,6)
print(day_of_the_week)
print()

print(calendar.isleap(2020))
print()
print(calendar.isleap(2019))


how_many_leap_days = calendar.leapdays(1900,2050)
print(how_many_leap_days)
