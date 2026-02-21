class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

class Calculator:
  def add(self, a, b):
    return a + b

calc = Calculator()
print(calc.add(5, 10))

class Player:
  def __init__(self, name):
    self.name = name
    self.score = 0

  def increase_score(self, points):
    self.score += points

p = Player("Alice")
p.increase_score(10)
print(p.score)

class Light:
  def __init__(self):
    self.on = False

  def toggle(self):
    self.on = not self.on

lamp = Light()
lamp.toggle()
print(lamp.on)

class Greeting:
  def say_hi(self, target):
    print(f"Hi {target}!")

g = Greeting()
g.say_hi("User")
