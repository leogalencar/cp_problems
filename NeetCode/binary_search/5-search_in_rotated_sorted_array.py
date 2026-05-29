# Solution with two binary searches: first to find the minimum element, then to find the target element in the correct half of the array.
# Time complexity: O(log n)
# Space complexity: O(1)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        min_pos = l
        l, r = 0, len(nums) - 1

        if target >= nums[min_pos] and target <= nums[r]:
            l = min_pos
        else:
            r = min_pos - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m

        return -1
