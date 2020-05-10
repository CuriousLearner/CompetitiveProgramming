# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 2, -1, -1):
            arr[i] = max(arr[i + 1], arr[i])
        return arr[1:] + [-1]
