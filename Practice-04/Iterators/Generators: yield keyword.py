def simple_gen():
    yield "A"
    yield "B"
    yield "C"

for val in simple_gen():
    print(val)

def step_gen():
    yield 10
    yield 20

g = step_gen()
print(next(g))
print(next(g))

def fruit_gen():
    yield "Apple"
    yield "Orange"

for f in fruit_gen():
    print(f)

def status_gen():
    yield True
    yield False

it = status_gen()
print(next(it))

def multi_yield():
    yield 1
    yield 2
    yield 3

print(sum(multi_yield()))
