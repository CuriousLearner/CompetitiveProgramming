import string


def word_count(phrase):
    phrase = "".join([letter if letter.isalnum() else " " for letter in phrase])
    word_list = phrase.lower().split()
    freq_dict = {word: 0 for word in word_list if word}
    for word in word_list:
        freq_dict[word] += 1
    return freq_dict
