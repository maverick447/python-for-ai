#import datetime
# alternatively u can import from datetime 
from datetime import date, time, datetime,timedelta 
today = date.today()
print(today)  # 2024-01-15
print(type(today))

print(today.year)
print(type(today.year))

print(today.month)
print(type(today.month))

print(today.day)
print(type(today.day))

now = datetime.now()
print(now)
print(type(now))

second = now.second
print(second)

numbers_of_days = 3
in_three_days = now + timedelta(days=numbers_of_days)
print(f"{numbers_of_days} days later: {in_three_days.strftime("%y-%m-%d")}")

# one_hour_ago = now - timedelta(hours=1)
# print("1 hour ago:", one_hour_ago)