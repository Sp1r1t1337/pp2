monitor = {"brand": "HP", "size": 27, "color": "Silver", "hz": 144}
monitor.pop("color")
print(monitor)

monitor.popitem()
print(monitor)

del monitor["brand"]
print(monitor)

monitor.clear()
print(monitor)

del monitor
# print(monitor) would cause an error
