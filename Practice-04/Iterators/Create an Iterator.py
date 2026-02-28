class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 5:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
  print(x)

class Countdown:
    def __init__(self, start):
        self.start = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.start > 0:
            val = self.start
            self.start -= 1
            return val
        raise StopIteration

for i in Countdown(3):
    print(i)

class PowerTwo:
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        result = 2 ** self.n
        self.n += 1
        if self.n > 4:
            raise StopIteration
        return result

print(list(PowerTwo()))

class Alphabet:
    def __iter__(self):
        self.char = 65
        return self
    def __next__(self):
        if self.char > 68:
            raise StopIteration
        res = chr(self.char)
        self.char += 1
        return res

for l in Alphabet():
    print(l)

class Repeat:
    def __init__(self, val, times):
        self.val = val
        self.times = times
    def __iter__(self):
        return self
    def __next__(self):
        if self.times > 0:
            self.times -= 1
            return self.val
        raise StopIteration

print(list(Repeat("Hi", 3)))
