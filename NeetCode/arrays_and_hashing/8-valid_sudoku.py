# not finished yet


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = c = 0
        rows = [set()] * 9
        columns = [set()] * 9
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

            print(rows)
            c += 1

        return True
