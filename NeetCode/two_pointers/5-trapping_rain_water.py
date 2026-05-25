# Solution with two pointers, one from the left and one from the right. We keep track of the maximum height on both sides and calculate the trapped water based on the minimum of the two maximum heights minus the current height at the pointer. We move the pointer that has the smaller maximum height towards the center until they meet.
# Time complexity: O(n)
# Space complexity: O(1)


class Solution:
    def trap(self, height: List[int]) -> int:
        # area between l and r for pos i = min(height[l], height[r]) - height[i]

        res = 0
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]

        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                res += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                res += maxRight - height[r]
        return res
