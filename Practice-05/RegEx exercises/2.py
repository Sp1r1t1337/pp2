import re
def match_a_two_three_b(text):
    return re.findall(r'ab{2,3}', text)

txt = input(str("Enter string: "))
print(match_a_two_three_b(txt))
