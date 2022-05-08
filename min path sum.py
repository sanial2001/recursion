class Solution:
    def solve(self, grid, row, col, path_sum, visited):
        if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or visited[row][col] == True or path_sum > self.res:
            return
        if row == len(grid)-1 and col == len(grid[0])-1:
            path_sum = path_sum + grid[row][col]
            #print(path_sum)
            self.res = min(self.res, path_sum)
            return
        visited[row][col] = True
        self.solve(grid, row - 1, col, path_sum + grid[row][col], visited)
        self.solve(grid, row, col - 1, path_sum + grid[row][col], visited)
        self.solve(grid, row + 1, col, path_sum + grid[row][col], visited)
        self.solve(grid, row, col + 1, path_sum + grid[row][col], visited)
        visited[row][col] = False

    def minPathSum(self, grid):
        path_sum, self.res = 0, 10000
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        self.solve(grid, 0, 0, path_sum, visited)
        return self.res


if __name__ == '__main__':
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(Solution().minPathSum(grid))

