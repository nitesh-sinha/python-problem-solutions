# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
#
# Example 1:
# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
#
# Example 2:
#
# Input: board =
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8.
# Since there are two 8's in the top left 3x3 sub-box, it is invalid.
#
#
# Constraints:
#
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.
#


class Validator:
    def is_valid_sudoku(self, board: list[list[str]]) -> bool:
        seen: set = {""}
        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    row_encoding = f'{board[row][col]} in row {row}'
                    col_encoding = f'{board[row][col]} in col {col}'
                    box_encoding = f'{board[row][col]} in box {row // 3}.{col // 3}'
                    if row_encoding in seen or col_encoding in seen or box_encoding in seen:
                        return False
                    seen.update([row_encoding, col_encoding, box_encoding])
        return True


if __name__ == "__main__":
    v = Validator()
    board = [["8","2","7","1","5","4","3","9","6"],
             ["9","6","5","3","2","7","1","4","8"],
             ["3","4","1","6","8","9","7","5","2"],
             ["5","9","3","4","6","8","2","7","1"],
             ["4","7","2","5","1","3","6","8","9"],
             ["6","1","8","9","7","2","4","3","5"],
             ["7","8","6","2","3","5","9","1","4"],
             ["1","5","4","7","9","6","8","2","3"],
             ["2","3","9","8","4","1","5","6","7"]]
    print(v.is_valid_sudoku(board))