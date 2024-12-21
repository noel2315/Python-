from datetime import datetime
now=datetime.now()
print(now)

from datetime import datetime
now=datetime.today()
print(now)

import calendar
y = int(input("Enter the Year :"))
print(calendar.prcal(y))

import calendar
y = int(input("Enter the Year :"))
m=int(input("Enter the month :"))
print(calendar.month(y,m))

import numpy as np
print("Number of weekdays in March 2017:",
      np.busday_count('2017-03', '2017-04'))

  
print("Number of Sunday in november 2020:",
      np.busday_count('2020-11', '2020-12',weekmask='Sun'))
yearMonth = '2017-05'
  
date = np.busday_offset(yearMonth, 0, roll='forward',weekmask='Mon')
print(date)

