# https://leetcode.com/problems/word-break/


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        is_word_break = [False] * (len(s) + 1)
        is_word_break[0] = True
        for i in range(len(s) + 1):
            for j in range(i):
                if is_word_break[j] and s[j:i] in wordDict:
                    is_word_break[i] = True
                    break
        return is_word_break[-1]
