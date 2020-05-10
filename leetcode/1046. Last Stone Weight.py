# https://leetcode.com/problems/last-stone-weight/

import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            fs = abs(heapq.heappop(stones))
            sc = abs(heapq.heappop(stones))
            if fs != sc:
                heapq.heappush(stones, -abs(sc - fs))

        return abs(stones[0]) if stones else 0
