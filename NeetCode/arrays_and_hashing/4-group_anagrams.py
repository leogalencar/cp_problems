# Solution with counting characters instead of sorting the string. This is more efficient since we only need to iterate through the string once, while sorting would require O(n log n) time.
# Time complexity: O(n * k), where n is the number of strings and k is the maximum length of a string.
# Space complexity: O(n * k).


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}

        for i in range(len(strs)):
            s = strs[i]
            chars = [0] * 26
            for j in range(len(s)):
                c = s[j]
                chars[ord(c) - ord("a")] += 1
            chars_s = "".join(str(chars))
            if chars_s in hmap:
                hmap[chars_s].append(s)
            else:
                hmap[chars_s] = [s]

        return list(hmap.values())
