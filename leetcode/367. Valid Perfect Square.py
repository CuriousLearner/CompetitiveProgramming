# https://leetcode.com/problems/valid-perfect-square/


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        rem = num % 10
        if rem in (2, 3, 7, 8):
            # Perfect squares cannot end in these digits
            return False
        l = 1
        r = num
        while l <= r:
            mid = int(l + (r - l) // 2)
            sq = mid * mid
            if sq == num:
                return True
            elif sq < num:
                l = mid + 1
            else:
                r = mid - 1
        return False
