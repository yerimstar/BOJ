import datetime
import sys
daylist = ['MON','TUE','WED','THU','FRI','SAT','SUN']
m,d = map(int,sys.stdin.readline().split())
print(daylist[datetime.date(2007,m,d).weekday()])