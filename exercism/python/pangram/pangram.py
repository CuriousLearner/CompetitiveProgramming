import string

def is_pangram(text):
    alphabet_list = [character for character in string.ascii_lowercase]
    char_list = [character for character in text if character.isalpha()]
    if alphabet_list == char_list:
        return True
    return False
    # pangram_dict = {ord(character): 0 for character in string.ascii_lowercase}
    # for key in set(text.lower()):
    #     try:
    #         pangram_dict[ord(key)] += 1
    #     except KeyError:
    #         pangram_dict[ord(key)] = -1
    # for key in string.ascii_lowercase:
    #     if pangram_dict[ord(key)] == 0:
    #         return False
    # return True
