class Mammal:
  def walk(self):
    print("Walking")

class Bird:
  def fly(self):
    print("Flying")

class Bat(Mammal, Bird):
  pass

b = Bat()
b.walk()
b.fly()

class Father:
  f_name = "John"

class Mother:
  m_name = "Jane"

class Child(Father, Mother):
  pass

c = Child()
print(c.f_name, c.m_name)

class Engine:
  def start_engine(self):
    print("Engine started")

class Radio:
  def play_music(self):
    print("Playing music")

class LuxuryCar(Engine, Radio):
  pass

car = LuxuryCar()
car.start_engine()
car.play_music()

class Calculation1:
  def add(self, a, b):
    return a + b

class Calculation2:
  def multiply(self, a, b):
    return a * b

class Calculator(Calculation1, Calculation2):
  pass

calc = Calculator()
print(calc.add(2, 3), calc.multiply(2, 3))

class LogicA:
  a = True

class LogicB:
  b = False

class LogicResult(LogicA, LogicB):
  pass

res = LogicResult()
print(res.a, res.b)
