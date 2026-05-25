# Solution with a set to achieve O(n) time complexity. We iterate through the set of numbers and for each number that is the start of a sequence (i.e., n - 1 is not in the set), we count how long the sequence is by checking for consecutive numbers. We keep track of the maximum count found.
# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count = 0
        nums_set = set(nums)

        for n in nums_set:
            if (n - 1) not in nums_set:
                count = 1
                while (n + count) in nums_set:
                    count += 1
                max_count = max(max_count, count)

        return max_count
