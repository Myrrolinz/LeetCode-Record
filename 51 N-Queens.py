class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        chessboard = ['.' * n for _ in range(n)]
        self.backtracking(n, 0, chessboard, result)
        return [[''.join(row) for row in solution] for solution in result]

    def backtracking(self, n, row, chessboard, result):
        if row == n:
            result.append(chessboard[:])
            return
        for col in range(n):
            if self.isValid(row, col, chessboard):
                chessboard[row] = chessboard[row][:col] + 'Q' + chessboard[row][col+1:]
                self.backtracking(n, row+1, chessboard, result)
                chessboard[row] = chessboard[row][:col] + '.' + chessboard[row][col+1:]
                
    def isValid(self, row: int, col: int, chessboard: List[str]) -> bool:
        # 检查列
        for i in range(row):
            if chessboard[i][col] == 'Q':
                return False  # 当前列已经存在皇后，不合法

        # 检查 45 度角是否有皇后
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if chessboard[i][j] == 'Q':
                return False  # 左上方向已经存在皇后，不合法
            i -= 1
            j -= 1

        # 检查 135 度角是否有皇后
        i, j = row - 1, col + 1
        while i >= 0 and j < len(chessboard):
            if chessboard[i][j] == 'Q':
                return False  # 右上方向已经存在皇后，不合法
            i -= 1
            j += 1

        return True  # 当前位置合法