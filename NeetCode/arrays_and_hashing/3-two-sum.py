# Solution with hmap and complement logic
# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if nums[i] in complements.keys():
                return [complements[nums[i]], i]
            complements[complement] = i
