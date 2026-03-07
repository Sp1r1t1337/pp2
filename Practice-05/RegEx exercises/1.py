import re
def match_a_zero_plus_b(text):
    pattern = r'ab*'
    if re.search(pattern, text):
        return "Found a match!"
    return "No match found."
