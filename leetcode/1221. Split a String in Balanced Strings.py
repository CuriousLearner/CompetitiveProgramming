# https://leetcode.com/problems/split-a-string-in-balanced-strings/


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = 0
        cnt_init = 0
        for char in s:
            if char == "R":
                cnt_init += 1
            else:
                cnt_init -= 1
            if cnt_init == 0:
                cnt += 1
        return cnt
