class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
print(p1.name)

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

my_car = Car("Ford", "Mustang")
print(my_car.model)

class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

b1 = Book("1984", "George Orwell")
print(b1.author)

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

pt = Point(10, 20)
print(pt.x, pt.y)

class Product:
  def __init__(self, id, price):
    self.id = id
    self.price = price

item = Product(101, 29.99)
print(item.price)
