import re
def find_underscore_sequences(text):
    return re.findall(r'[a-z]+_[a-z]+', text)

txt = input(str("Enter string: "))
print(find_underscore_sequences(txt))
