import datetime

d1 = datetime.datetime(2026, 1, 1)
d2 = datetime.datetime(2026, 1, 10)
diff = d2 - d1
print(diff.days)

now = datetime.datetime.now()
future = now + datetime.timedelta(days=30)
print(future)

past = now - datetime.timedelta(weeks=2)
print(past)

duration = datetime.timedelta(hours=5, minutes=30)
print(duration.total_seconds())

birth = datetime.date(1990, 5, 15)
today = datetime.date.today()
age_days = today - birth
print(age_days.days // 365)
