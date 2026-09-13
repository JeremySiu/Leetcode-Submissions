from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_arr = [0 for _ in range(81)]
        for i in range(9):
            row_arr = [0 for _ in range(9)]
            if i % 3 == 0:
                square_arr = [0 for _ in range(27)]
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                elif int(val) > 9 or int(val) < int(1):
                    return False
                else:
                    idx = int(val) - 1
                    row_arr[idx] += 1
                    column_arr[j*9 + idx] += 1
                    square_arr[(j//3)*9 + idx] += 1

                    if row_arr[idx] > 1 or column_arr[j*9 + idx] > 1 or square_arr[(j//3)*9 + idx] > 1:
                        return False
        return True