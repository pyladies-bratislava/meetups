# Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14
from datetime import datetime
from dateutil import tz


timezone = tz.gettz('Australia/Sydney')
print(datetime.now(tz=timezone).strftime("%d.%m.%Y %H:%M:%S.%f %Z"))
