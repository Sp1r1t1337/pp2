import re
def split_at_upper(text):
    return re.split(r'(?=[A-Z])', text)

txt = input(str("Enter string: "))
print(split_at_upper(txt))
