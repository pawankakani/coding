import datetime
import datetime as d ## <1>
from datetime import datetime as di
import calendar

print(datetime.datetime.today()) # use 1st module import, print current date/time
print(d.datetime.today()) # 2nd import, print current date/time
print(di.today().ctime()) # 3rd import, print current date/time

mydate = di(2021, 6, 27, 18, 55, 5)
print(mydate)
print(mydate.ctime())
print(di.now())

tc = calendar.TextCalendar()
tc.prmonth(2021,6)
