# Solution with monotonic stack to find the largest rectangle in a histogram.
# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        stack = []
        leftIndex = [-1] * n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftIndex[i] = stack[-1]
            stack.append(i)

        stack = []
        rightIndex = [n] * n
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightIndex[i] = stack[-1]
            stack.append(i)

        maxArea = 0
        for i in range(n):
            area = heights[i] * (rightIndex[i] - leftIndex[i] - 1)
            maxArea = max(maxArea, area)

        return maxArea
