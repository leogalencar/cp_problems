# Solution with O(n) time complexity and O(1) space complexity using the Floyd's Tortoise and Hare algorithm (Cycle Detection).
# Time complexity: O(n)
# Space complexity: O(1)


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
