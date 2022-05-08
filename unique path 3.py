class Solution:
    def dfs(self, grid, row, col, cnt, zero):
        if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or grid[row][col] == -1:
            return
        cnt += 1 if grid[row][col] == 0 else 0
        if grid[row][col] == 2:
            if cnt == zero:
                self.ans += 1
            return
        grid[row][col] = -1
        self.dfs(grid, row - 1, col, cnt, zero)
        self.dfs(grid, row, col - 1, cnt, zero)
        self.dfs(grid, row + 1, col, cnt, zero)
        self.dfs(grid, row, col + 1, cnt, zero)
        grid[row][col] = 0

    def uniquePathsIII(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        zero = 0
        self.ans = 0
        starti, startj = -1, -1
        endi, endj = -1, -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    zero += 1
                elif grid[i][j] == 1:
                    starti, startj = i, j
                elif grid[i][j] == 2:
                    endi, endj = i, j
        self.dfs(grid, starti, startj, 0, zero)
        return self.ans
