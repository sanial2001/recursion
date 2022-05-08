class Solution:
    def is_valid(self, r, c):
        for i in range(9):
            if board[r][i] == str(i):
                return False
            if board[i][c] == str(i):
                return False

    def solveSudoku(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for k in range(9):
                        board[row][col] = str(k)
                        if self.is_valid(row, col) == True:



if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    Solution().solveSudoku(board)
