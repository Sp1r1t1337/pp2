class Animal:
  def move(self):
    print("Moving...")

class Bird(Animal):
  def move(self):
    print("Flying...")

b = Bird()
b.move()

class Phone:
  def call(self):
    print("Dialing...")

class SmartPhone(Phone):
  def call(self):
    print("Video Calling...")

sp = SmartPhone()
sp.call()

class Robot:
  def task(self):
    print("General tasks")

class CleaningRobot(Robot):
  def task(self):
    print("Cleaning floors")

bot = CleaningRobot()
bot.task()

class Employee:
  def get_pay(self):
    return 1000

class Manager(Employee):
  def get_pay(self):
    return 2000

m = Manager()
print(m.get_pay())

class Printer:
  def show(self):
    print("Printing Black & White")

class ColorPrinter(Printer):
  def show(self):
    print("Printing Color")

cp = ColorPrinter()
cp.show()
