#1
from datetime import datetime, timedelta

current_date = datetime.now()
result_date = current_date - timedelta(days=5)

print("Current Date:", current_date.strftime("%Y-%m-%d"))
print("5 days ago:", result_date.strftime("%Y-%m-%d"))


#2
from datetime import date, timedelta

today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#3
from datetime import datetime

dt = datetime.now()
# Убираем микросекунды
dt_no_microseconds = dt.replace(microsecond=0)

print("With microseconds:", dt)
print("Without microseconds:", dt_no_microseconds)

#4
from datetime import datetime

# Пример двух дат
date1 = datetime(2026, 3, 7, 12, 0, 0)
date2 = datetime(2026, 3, 5, 12, 0, 0)

difference = date1 - date2
seconds_diff = difference.total_seconds()

print(f"Difference in seconds: {seconds_diff}")
