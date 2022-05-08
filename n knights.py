class Solution:
    def can_be_placed(self, board, row, col, n):
        i, j = row-2, col+1
        if i >= 0 and j < n:
            if board[i][j] == 1:
                return False

        i, j = row-1, col+2
        if i >= 0 and j < n:
            if board[i][j] == 1:
                return False

        i, j = row-1, col-2
        if i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False

        i, j = row-2, col-1
        if i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False

        return True

    def solve(self, board, row, col, n):
        if n == 0:
            '''for val in board:
                print(val)
            '''
            self.res = []
            for i in range(len(board)):
                ch = ''
                for j in range(len(board[0])):
                    if board[i][j] == 1:
                        ch = ch + 'K'
                    else:
                        ch = ch + '.'
                self.res.append(ch)
            self.ans.append(self.res)
            return

        print(row, col, n)
        for i in range(row, len(board)):
            for j in range(col, len(board[0])):
                #print(i, j, n)
                if self.can_be_placed(board, i, j, len(board)) == True:
                    board[i][j] = 1
                    if j == len(board):
                        self.solve(board, i+1, 0, n-1)
                    else:
                        self.solve(board, i, j+1, n-1)
                    board[i][j] = 0
        '''
        board[row][col] = 1
        if col == len(board):
            self.solve(board, row+1, 0, n - 1)
        else:
            self.solve(board, row, col+1, n-1)
        board[row][col] = 0
        '''

    def solveNKnights(self, n):
        board = [[0 for _ in range(n)] for _ in range(n)]
        self.res, self.ans = [], []
        self.solve(board, 0, 0, n)
        print(self.ans)


if __name__ == '__main__':
    Solution().solveNKnights(4)
