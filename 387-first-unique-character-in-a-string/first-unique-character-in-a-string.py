class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i
        return -1
        # for i, ch in enumerate(s):
        #     if s.count(ch) == 1:
        #         return i
        # return -1