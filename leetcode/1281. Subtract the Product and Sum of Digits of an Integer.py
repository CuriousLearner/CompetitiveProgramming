# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        summation = 0
        for dig in str(n):
            summation += int(dig)
            product *= int(dig)
        return product - summation
