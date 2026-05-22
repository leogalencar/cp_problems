class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)

        return True if len(s) != len(nums) else False
