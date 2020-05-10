# https://leetcode.com/problems/find-the-town-judge/


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1
        count = [0] * (N + 1)
        for t in trust:
            count[t[0]] -= 1
            count[t[1]] += 1
        for i, c in enumerate(count):
            if c == N - 1:
                return i
        return -1
