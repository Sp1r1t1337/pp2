def match_a_to_b(text):
    pattern = r'a.*b$'
    if re.search(pattern, text):
        return "Match found"
    return "No match"
