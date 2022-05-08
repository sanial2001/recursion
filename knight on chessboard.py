class Solution:
    def solve(self, board, C, D, E, F, cnt):
        #print(C, D)
        if C < 0 or D < 0 or C >= len(board) or D >= len(board[0]) or board[C][D] == 1:
            return
        elif C == E and D == F:
            print(cnt)
            return
        elif cnt == len(board) * len(board[0]):
            return
        board[C][D] = 1
        self.solve(board, C - 2, D + 1, E, F, cnt + 1)
        self.solve(board, C - 1, D + 2, E, F, cnt + 1)
        self.solve(board, C + 1, D + 2, E, F, cnt + 1)
        self.solve(board, C + 2, D + 1, E, F, cnt + 1)
        self.solve(board, C + 2, D - 1, E, F, cnt + 1)
        self.solve(board, C + 1, D - 2, E, F, cnt + 1)
        self.solve(board, C - 1, D - 2, E, F, cnt + 1)
        self.solve(board, C - 2, D - 1, E, F, cnt + 1)
        board[C][D] = 0

    def knight(self, A, B, C, D, E, F):
        board = [[0 for _ in range(B)] for _ in range(A)]
        cnt = 0
        self.solve(board, C-1, D-1, E-1, F-1, cnt)
        print(cnt)


if __name__ == '__main__':
    Solution().knight(8, 8, 1, 1, 8, 8)

