# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for num in nums:
            ch_cnt = 0
            for char in str(num):
                ch_cnt += 1
            if ch_cnt & 1 == 0:
                cnt += 1
        return cnt
