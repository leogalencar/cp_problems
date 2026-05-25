# Solution with two pointers, one starting from the beginning of the string and the other starting from the end of the string. We will move both pointers towards each other while skipping non-alphanumeric characters. If at any point the characters at both pointers do not match (ignoring case), we can conclude that the string is not a palindrome. If we successfully compare all characters without finding a mismatch, then the string is a palindrome.
# Time complexity: O(n) where n is the length of the string, since we may need to traverse the entire string in the worst case.
# Space complexity: O(1) since we are using only a constant amount of extra space for the pointers and temporary variables.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not str.isalnum(s[l]):
                l += 1
            while r > l and not str.isalnum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1

        return True
