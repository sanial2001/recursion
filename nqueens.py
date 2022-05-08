class Solution:
    def can_be_placed(self, place, row, col, n):
        i, j = row - 1, col
        while i >= 0:
            if place[i][j] == 1:
                return False
            i = i-1

        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if place[i][j] == 1:
                return False
            i, j = i-1, j-1

        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if place[i][j] == 1:
                return False
            i, j = i-1, j+1

        return True

    def solve(self, place, n, index):
        '''
        if index == n:
            self.result = []
            for i in range(n):
                ch = ''
                for j in range(n):
                    if place[i][j] == 0:
                        ch = ch + '.'
                    elif place[i][j] == 1:
                        ch = ch + 'Q'
                self.result.append(ch)
            self.ans.append(self.result)
            return
        '''
        if index == n:
            res = []
            for i in range(n):
                for j in range(n):
                    if place[i][j] == 1:
                        res.append(j+1)
            self.ans.append(res)
            return

        for col in range(n):
            if self.can_be_placed(place, index, col, n) == True:
                place[index][col] = 1
                self.solve(place, n, index + 1)
                place[index][col] = 0

    def solveNQueens(self, n):
        place = [[0 for _ in range(n)] for _ in range(n)]
        self.result = []
        self.ans = []
        self.solve(place, n, 0)
        print(self.ans)


if __name__ == '__main__':
    Solution().solveNQueens(4)
