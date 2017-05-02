def hey(phrase):
    phrase = phrase.strip()
    if phrase.isupper():
        return "Whoa, chill out!"
    elif phrase.endswith('?'):
        return "Sure."
    elif not phrase.split():
        return "Fine. Be that way!"
    else:
        return "Whatever."
