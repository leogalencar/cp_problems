# Solution with binary search. We can use the fact that the array is sorted to our advantage and perform a binary search to find the target element. We will keep track of the left and right pointers and calculate the middle index in each iteration. If the middle element is greater than the target, we will move the right pointer to the left of the middle index. If it is less than the target, we will move the left pointer to the right of the middle index. If we find the target element, we will return its index. If we exhaust all possibilities and do not find the target, we will return -1.
# Time complexity: O(log n)
# Space complexity: O(1)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1
