# https://leetcode.com/problems/maximum-69-number/


class Solution:
    def maximum69Number(self, num: int) -> int:
        return str(num).replace("6", "9", 1)
