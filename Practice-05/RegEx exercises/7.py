import re
def snake_to_camel(text):
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), text)

txt = input(str("Enter snake_case: "))
print(snake_to_camel(txt))
