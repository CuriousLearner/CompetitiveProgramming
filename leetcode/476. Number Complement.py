# https://leetcode.com/problems/number-complement/


class Solution:
    def findComplement(self, num: int) -> int:
        mask = 1
        while mask < num:
            mask = (mask << 1) + 1
        return mask ^ num
