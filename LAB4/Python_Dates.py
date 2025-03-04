#1 Subtract five days from the current date

from datetime import datetime, timedelta

current_date = datetime.today()
new_date = current_date - timedelta(days=5)

print(new_date)


#2 Print yesterday, today, and tomorrow
from datetime import datetime, timedelta

today = datetime.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print(yesterday)
print(today)
print(tomorrow)


#3 Drop microseconds from datetime
from datetime import datetime

now = datetime.now()
without_micro = now.replace(microsecond=0)  


print(without_micro)


#4 Calculate the difference between two dates in seconds
from datetime import datetime

date1 = datetime(2025, 3, 4, 12, 0, 0)  # Example date 1
date2 = datetime(2025, 3, 5, 12, 30, 0)  # Example date 2

difference = (date2 - date1).total_seconds()

print("Difference in seconds:", difference)








