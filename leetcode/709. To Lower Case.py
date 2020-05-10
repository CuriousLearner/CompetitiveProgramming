# https://leetcode.com/problems/to-lower-case/


class Solution:
    def toLowerCase(self, str: str) -> str:
        return "".join([chr(ord(c) | 32) for c in str])
