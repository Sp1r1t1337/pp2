import datetime

utc_now = datetime.datetime.now(datetime.timezone.utc)
print(utc_now)

est_offset = datetime.timezone(datetime.timedelta(hours=-5))
est_time = datetime.datetime.now(est_offset)
print(est_time)

current = datetime.datetime.now(datetime.timezone.utc)
local = current.astimezone()
print(local)

# Creating a timezone-aware object
aware_date = datetime.datetime(2026, 1, 1, tzinfo=datetime.timezone.utc)
print(aware_date.tzname())

# Tokyo offset example
jst_offset = datetime.timezone(datetime.timedelta(hours=9))
tokyo_time = datetime.datetime.now(jst_offset)
print(tokyo_time)
