from datetime import datetime
import time

dt1 = datetime(2018, 2, 5)
dt2 = datetime.now()
dt3 = datetime.strptime("2018/2/5", "%Y/%m/%d")
dt4 = datetime.fromtimestamp(time.time())

print(dt1)
print(dt2)
print(dt3)
print(dt4)