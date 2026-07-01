class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 0-8: row, 9-17:col, 18-26:block
        flag = []
        for _ in range(27):
            flag.append([])
        for row in range(len(board)):
            for col in range(len(board[row])):
                num = board[row][col]
                if num != '.':
                    # row
                    flag[row].append(num)
                    # col
                    flag[col+9].append(num)
                    # block
                    # print(row, col, row//3*3+col//3)
                    flag[row//3*3+(col//3)+18].append(num)
        for f in flag:
            if len(f) != len(set(f)):
                # print(f, set(f))
                return False
        return True
