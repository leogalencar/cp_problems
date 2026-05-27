# Solution with single-pass stack to find the largest rectangle in a histogram.
# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        n = len(heights)
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append([start, h])

        for i, h in stack:
            maxArea = max(maxArea, h * (n - i))

        return maxArea
