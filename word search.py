class Solution:
    def solve(self, board, row, col, word, index, visited, res):
        if row < 0 or col < 0 or row == len(board) or col == len(board[0]) or visited[row][col] == True or board[row][col] != word[index]:
            return
        if index == len(word)-1:
            res[0] = True
            return
        visited[row][col] = True
        self.solve(board, row-1, col, word, index+1, visited, res)
        self.solve(board, row, col-1, word, index+1, visited, res)
        self.solve(board, row+1, col, word, index+1, visited, res)
        self.solve(board, row, col+1, word, index+1, visited, res)
        visited[row][col] = False

    def exist(self, board, word):
        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res = [False]
                if board[i][j] != word[0]:
                    continue
                self.solve(board, i, j, word,  0, visited, res)
                if res[0] is True:
                    return True
        return False


if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    Solution().exist(board, word)