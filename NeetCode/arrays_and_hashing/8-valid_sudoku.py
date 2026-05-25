# Solution with 3x3 square passes and sets to check for duplicates in rows, columns, and 3x3 squares.
# Time complexity: O(n^2)
# Space complexity: O(n)


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = c = 0
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        for i in range(9):
            if i != 0 and i % 3 == 0:
                r += 1
                c = 0
            square = set()
            for j in range(3):
                for k in range(3):
                    current = board[j + 3 * r][k + 3 * c]
                    if current != "." and current in square:
                        return False
                    square.add(current)

                    if current != "." and current in rows[j + 3 * r]:
                        return False
                    rows[j + 3 * r].add(current)

                    if current != "." and current in cols[k + 3 * c]:
                        return False
                    cols[k + 3 * c].add(current)
            c += 1

        return True
