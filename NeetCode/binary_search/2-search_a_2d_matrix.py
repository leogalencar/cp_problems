# Solution with binary search within the matrix, first to find the row and then to find the target within that row.
# Time complexity: O(log m + log n)
# Space complexity: O(1)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # using binary search within the matrix
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][-1] < target:
                l = m + 1
            else:
                l2, r2 = 0, len(matrix[m])
                while l2 <= r2:
                    m2 = l2 + ((r2 - l2) // 2)

                    if matrix[m][m2] > target:
                        r2 = m2 - 1
                    elif matrix[m][m2] < target:
                        l2 = m2 + 1
                    else:
                        return True
                return False
        return False
