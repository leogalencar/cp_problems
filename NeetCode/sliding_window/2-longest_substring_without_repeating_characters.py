# Solution with sliding window technique.
# Time complexity: O(n) where n is the length of the input string.
# Space complexity: O(min(m, n)) where m is the size of the character set.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)

        return res
