# Solution with two pointers approach. We start with two pointers, one at the beginning of the array and one at the end. We calculate the area formed by the lines at these two pointers and update our result if it's larger than the previous maximum area. Then, we move the pointer that has the smaller height towards the center, since moving the taller pointer won't increase the area. We repeat this process until the two pointers meet.
# Time complexity: O(n)
# Space complexity: O(1)


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        # width is calculated by r - l
        # height is calculated by min(heights[r], heights[l])
        # area is calculated by width * height

        l, r = 0, len(heights) - 1

        while l < r:
            width = r - l
            height = min(heights[r], heights[l])
            area = width * height

            res = max(res, area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return res
