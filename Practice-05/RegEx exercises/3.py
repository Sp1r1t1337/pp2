def find_underscore_sequences(text):
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern, text)
