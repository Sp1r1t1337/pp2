import re
def find_upper_lower(text):
    return re.findall(r'[A-Z][a-z]+', text)

txt = input(str("Enter string: "))
print(find_upper_lower(txt))
