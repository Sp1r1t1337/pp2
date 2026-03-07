import re
def match_a_zero_plus_b(text):
    if re.fullmatch(r'ab*', text):
        return "Found a match!"
    return "No match found."

txt = input(str("Enter string: "))
print(match_a_zero_plus_b(txt))
