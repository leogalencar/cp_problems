# Solution with binary search to find the minimum element in a rotated sorted array.
# Time complexity: O(log n)
# Space complexity: O(1)


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = l + ((r - l) // 2)

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

            res = min(res, nums[m])

        return res
