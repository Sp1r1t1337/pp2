class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  call_name = lambda self: print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.call_name()

class Animal:
  def eat(self):
    print("Eating...")

class Dog(Animal):
  def bark(self):
    print("Barking...")

d = Dog()
d.eat()

class Vehicle:
  brand = "Toyota"

class Car(Vehicle):
  model = "Camry"

my_car = Car()
print(my_car.brand)

class Shape:
  color = "Red"

class Square(Shape):
  side = 4

sq = Square()
print(sq.color)

class Tool:
  def use(self):
    print("Tool used")

class Hammer(Tool):
  pass

h = Hammer()
h.use()
