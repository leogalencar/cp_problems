# Solution with {length}#{string} format for encoding and decoding strings.
# Time complexity: O(n) where n is the total length of the encoded string.
# Space complexity: O(n) for storing the encoded string and the decoded list of strings.


class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decoded.append(s[i:j])
            i = j

        return decoded
