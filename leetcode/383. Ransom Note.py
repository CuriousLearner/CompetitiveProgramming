# https://leetcode.com/problems/ransom-note/

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = Counter(ransomNote)
        mag_freq = Counter(magazine)
        for k, v in freq.items():
            if v > mag_freq.get(k, 0):
                return False

        return True
