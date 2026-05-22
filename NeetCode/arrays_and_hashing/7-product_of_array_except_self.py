# Solution with prefix and suffix products to calculate the product of all elements except self without using division.
# Time complexity: O(n) for iterating through the list twice to calculate the prefix and suffix products.
# Space complexity: O(n) for the output list, which is required to store the results.


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_n = len(nums)
        answer = [1] * len_n
        all_left_products = 1
        for i in range(len_n):
            answer[i] = all_left_products
            all_left_products *= nums[i]

        all_right_products = 1
        for j in range(len_n - 1, -1, -1):
            answer[j] *= all_right_products
            all_right_products *= nums[j]

        return answer
