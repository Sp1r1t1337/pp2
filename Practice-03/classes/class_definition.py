class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

class Device:
  brand = "Generic"

phone = Device()
print(phone.brand)

class Empty:
  pass

obj = Empty()
print(type(obj))

class Room:
  status = "Vacant"

living_room = Room()
print(living_room.status)

class User:
  is_logged_in = False

current_user = User()
print(current_user.is_logged_in)
