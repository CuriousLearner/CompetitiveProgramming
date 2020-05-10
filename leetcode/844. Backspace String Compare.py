# https://leetcode.com/problems/backspace-string-compare/


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def emulate_backspace(string):
            res = []
            for char in string:
                if char != "#":
                    res.append(char)
                elif res:
                    res.pop()
            return "".join(res)

        return emulate_backspace(S) == emulate_backspace(T)
