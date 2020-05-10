# https://leetcode.com/problems/counting-elements/


class Solution:
    def countElements(self, arr: List[int]) -> int:
        hmap = {}
        for x in arr:
            hmap[x] = hmap.get(x, 0) + 1
        count = 0
        for x in arr:
            if x + 1 in hmap:
                count += 1
        return count
