# https://leetcode.com/problems/happy-number/


class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        res = 0
        while int(n) != 1 and int(n) != 4:
            for x in n:
                res += pow(int(x), 2)
            n = str(res)
            res = 0
        if int(n) == 1:
            return True
        return False
