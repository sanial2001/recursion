class Solution:
    def check(self, board, row, col, val):
        for i in range(9):
            if board[row][i] == val:
                return False

        for i in range(9):
            if board[i][col] == val:
                return False

        for i in range(3):
            for j in range(3):
                if board[(row//3 * 3) + i][(col//3 * 3) + j] == val:
                    return False

        return True

    def solve(self, board, index, col, ans):
        if col == len(board):
            index, col = index+1, 0
            if index == len(board):
                for i in range(9):
                    for j in range(9):
                        ans[i][j] = str(board[i][j])
                return
        #print(index, col)
        if board[index][col] == 0:
            for i in range(1, 10):
                if self.check(board, index, col, i) == True:
                    board[index][col] = i
                    self.solve(board, index, col+1, ans)
                    board[index][col] = 0
        else:
            self.solve(board, index, col+1, ans)

    def solveSudoku(self, board) -> None:
        ans = [[0 for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    board[i][j] = 0
                else:
                    board[i][j] = int(board[i][j])

        self.solve(board, 0, 0, ans)

        for i in range(9):
            for j in range(9):
                board[i][j] = ans[i][j]

        for val in board:
            print(val)



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
    
