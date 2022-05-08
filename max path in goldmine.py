class Solution:
    def solve(self, grid, row, col, path_sum, ans, visited):
        if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or visited[row][col] == True or grid[row][col] == 0:
            return
        path_sum += grid[row][col]
        ans.append(path_sum)
        #print(path_sum, ans)
        visited[row][col] = True
        self.solve(grid, row-1, col, path_sum, ans, visited)
        self.solve(grid, row, col-1, path_sum, ans, visited)
        self.solve(grid, row+1, col, path_sum, ans, visited)
        self.solve(grid, row, col+1, path_sum, ans, visited)
        visited[row][col] = False
        path_sum -= grid[row][col]

    def getMaximumGold(self, grid):
        m, n = len(grid), len(grid[0])
        ans = []
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                self.solve(grid, i, j, 0, ans, visited)
        return max(ans)


if __name__ == '__main__':
    grid = [[0,6,0],[5,8,7],[0,9,0]]
    Solution().getMaximumGold(grid)
