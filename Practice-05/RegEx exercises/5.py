import re
def match_a_to_b(text):
    if re.search(r'a.*b$', text):
        return "Found a match!"
    return "No match found."

txt = input(str("Enter string: "))
print(match_a_to_b(txt))
