import re
from itertools import groupby


def decode(phrase):
    group_list = [re.findall(r'\d+|\w+|\s+', x) for x in re.findall(r'\d*\s+|\d+\w?|\w?', phrase) if re.findall(r'\d+|\w+|\s+', x)]
    return "".join(map(lambda x: x[0] if x[0].isalpha() or x[0].isspace() else int(x[0]) * x[1], group_list))

def encode(phrase):
    run_length_groups = [list(char_group) for char, char_group in groupby(phrase)]
    return "".join(map(lambda char_list: char_list[0] if len(char_list) == 1 else str(len(char_list)) + char_list[0], run_length_groups))
