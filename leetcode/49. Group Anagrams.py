# https://leetcode.com/problems/group-anagrams/


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for word in strs:
            # For ordinals to work, a perfect hash has to be made.
            # Using prime numbers to avoid collision
            # anagram_key = sum([ord(letter) for letter in word])
            anagram_key = "".join(letter for letter in sorted(word))
            hmap[anagram_key] = hmap.get(anagram_key, []) + [word]
        return list(hmap.values())
