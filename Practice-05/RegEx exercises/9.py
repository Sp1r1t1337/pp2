import re
def insert_spaces(text):
    return re.sub(r'(\w)([A-Z])', r'\1 \2', text)

txt = input(str("Enter string: "))
print(insert_spaces(txt))
