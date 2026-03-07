def match_a_two_three_b(text):
    pattern = r'ab{2,3}'
    return re.findall(pattern, text)
