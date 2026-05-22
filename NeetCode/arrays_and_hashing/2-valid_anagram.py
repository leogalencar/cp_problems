# Solution with char counting with two arrays.
# Time complexity: O(n)
# Space complexity: O(1)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_s = [0] * 26
        char_t = [0] * 26

        for c in s:
            char_s[ord(c) - ord("a")] += 1

        for c in t:
            char_t[ord(c) - ord("a")] += 1

        return char_s == char_t
