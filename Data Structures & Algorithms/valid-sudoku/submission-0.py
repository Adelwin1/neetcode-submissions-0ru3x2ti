class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        square= [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == '.':
                    continue
                sq = (row // 3) * 3 + (col // 3)

                if (val in rows[row] or
                   val in cols[col] or 
                   val in square[sq]):
                   return False
                rows[row].add(val)
                cols[col].add(val)
                square[sq].add(val)
        return True
