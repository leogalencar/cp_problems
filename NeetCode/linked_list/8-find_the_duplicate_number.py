# Solution with O(n) time complexity and O(1) space complexity using the input array to track visited numbers.
# Time complexity: O(n)
# Space complexity: O(1)


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                return abs(num)
            nums[idx] *= -1
        return -1
