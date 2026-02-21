speed = 60
def show_speed():
    print(speed)
show_speed()

level = 1
def update_level():
    global level
    level = 2
update_level()
print(level)

def set_mode():
    global mode
    mode = "Dark"
set_mode()
print(mode)

username = "Guest"
def greet():
    username = "Admin"
    print(username)
greet()
print(username)

limit = 100
def check_limit():
    print(limit)
check_limit()
