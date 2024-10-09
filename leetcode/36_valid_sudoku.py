"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.

"""
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Iterative solution, needs to be fixed
        rows = {i: [] for i in range(9)}
        cols = {j: [] for j in range(9)}
        curr_square = []
        i, j = 0, 0

        while i <= 8 and j <= 8:
            if board[i][j] not in rows[i]:
                rows[i].append(board[i][j])
            else:
                return False

            if board[i][j] not in cols[j]:
                cols[j].append(board[i][j])
            else:
                return False

            if board[i][j] not in curr_square:
                curr_square.append(board[i][j])
            else:
                return False

            if (i + 1) % 3 == 0 and (j + 1) % 3:
                if i == 8 and j != 8:
                    i += 1
                    j = 0
                else:
                    j += 1
                    i -= 2
                curr_square = []
            elif (j + 1) % 3 == 0:
                j -= 2
                i += 1
            else:
                j += 1

        return True

    def isValidSudoku_bitwise(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for i in range(len(board)):
            for j in range(len(board)):
                value = board[i][j]

                if value == ".":
                    continue

                mask = 1 << (int(value) - 1)
                square_ind = (i // 3) * 3 + (j // 3)
                if (rows[i] & mask) or (cols[j] & mask) or (squares[square_ind] & mask):
                    return False

                rows[i] |= mask
                cols[j] |= mask
                squares[square_ind] |= mask

        return True
