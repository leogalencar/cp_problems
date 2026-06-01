# Solution with sliding window and frequency map to keep track of the count of characters in the current window.
# Time complexity: O(n) where n is the length of the string.
# Space complexity: O(m) where m is the number of unique characters in the string.


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxf = max(maxf, freq[s[r]])
            while (r - l + 1) - maxf > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
