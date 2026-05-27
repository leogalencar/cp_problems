# Solution with single pass binary search on a 2D matrix. We treat the matrix as a 1D array and calculate the corresponding row and column indices based on the middle index.
# Time complexity: O(log(m * n))
# Space complexity: O(1)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        l, r = 0, (ROWS * COLS) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            row = m // COLS
            col = m % COLS

            if matrix[row][col] > target:
                r = m - 1
            elif matrix[row][col] < target:
                l = m + 1
            else:
                return True
        return False
