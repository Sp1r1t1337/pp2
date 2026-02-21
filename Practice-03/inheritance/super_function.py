class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)

class Parent:
  def __init__(self, txt):
    self.message = txt

class Child(Parent):
  def __init__(self, txt):
    super().__init__(txt)

c = Child("Hello from Parent")
print(c.message)

class Computer:
  def __init__(self):
    self.power = "On"

class Laptop(Computer):
  def __init__(self):
    super().__init__()
    self.battery = "100%"

mac = Laptop()
print(mac.power)

class A:
  def greet(self):
    print("Hello from A")

class B(A):
  def greet(self):
    super().greet()
    print("Hello from B")

obj = B()
obj.greet()

class Base:
  def __init__(self, name):
    self.name = name

class Sub(Base):
  def __init__(self, name, age):
    super().__init__(name)
    self.age = age

s = Sub("Alice", 25)
print(s.name)
