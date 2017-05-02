def is_isogram(text):
    ordinals = [ord(x) for x in text.lower() if 97 <= ord(x) <= 122]
    return len(ordinals) == len(set(ordinals))
