class Dog:
  species = "Canine"
  def __init__(self, name):
    self.name = name

d1 = Dog("Rex")
print(d1.species)

class Employee:
  company = "TechCorp"
  def __init__(self, name):
    self.name = name

e1 = Employee("Bob")
print(e1.company)

class Circle:
  pi = 3.14
  def __init__(self, radius):
    self.radius = radius

c1 = Circle(5)
print(Circle.pi)

class Game:
  version = 1.0
  def __init__(self, title):
    self.title = title

my_game = Game("Quest")
print(Game.version)

class Student:
  school_name = "W3Schools Academy"
  def __init__(self, student_id):
    self.student_id = student_id

s1 = Student(123)
print(s1.school_name)
