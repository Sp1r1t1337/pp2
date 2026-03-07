import re
def camel_to_snake(text):
    res = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', res).lower()

txt = input(str("Enter CamelCase: "))
print(camel_to_snake(txt))
