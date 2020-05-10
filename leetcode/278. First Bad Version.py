# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        start = 1
        end = n
        while start < end:
            mid = ((end - start) // 2) + start
            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1

        return start
