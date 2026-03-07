def find_upper_lower(text):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, text)
