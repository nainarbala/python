from datetime  import datetime, timedelta
import time

dt1 = datetime(208,1,2) + timedelta(days=1, seconds=1000)
print(dt1)

dt2 = datetime.now()

duration = dt2 - dt1
print("days:=", duration.days)
print("sec:-", duration.seconds)
print("tol sec", duration.total_seconds())