import re
def replace_chars(text):
    return re.sub(r'[ ,.]', ':', text)

txt = input(str("Enter string: "))
print(replace_chars(txt))
