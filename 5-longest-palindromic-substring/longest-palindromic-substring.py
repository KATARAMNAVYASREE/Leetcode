class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        long_palin = ""
        for i in range(len(s)):
            odd=expand(i,i)
            even=expand(i,i+1)
            if len(odd)>len(long_palin):
                long_palin=odd
            if len(even)>len(long_palin):
                long_palin=even
        return long_palin