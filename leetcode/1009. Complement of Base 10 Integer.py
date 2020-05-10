# https://leetcode.com/problems/complement-of-base-10-integer/


class Solution:
    def bitwiseComplement(self, N: int) -> int:
        c = 1
        while c < N:
            c = (c << 1) + 1
        return N ^ c
