import datetime

d1 = datetime.datetime(2026, 5, 17)
print(d1)

d2 = datetime.datetime(2025, 12, 25, 18, 0, 0)
print(d2)

d3 = datetime.date(1995, 1, 1)
print(d3)

d4 = datetime.datetime.fromisoformat('2026-01-01T10:00:00')
print(d4)

d5 = datetime.datetime.strptime("21/06/24 16:30", "%d/%m/%y %H:%M")
print(d5)
