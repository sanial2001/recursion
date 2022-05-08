class Solution:
    def solve(self, height, row, col, path, ans, visited):
        if row < 0 or col < 0 or row == len(height) or col == len(height[0]) or visited[row][col] == True:
            return
        path.append(height[row][col])
        if row == len(height)-1 and col == len(height[0])-1:
            print(path)
            res = 0
            for i in range(1, len(path)):
                res = max(res, abs(path[i]-path[i-1]))
            ans.append(res)
        visited[row][col] = True
        self.solve(height, row-1, col, path, ans, visited)
        self.solve(height, row, col-1, path, ans, visited)
        self.solve(height, row+1, col, path, ans, visited)
        self.solve(height, row, col+1, path, ans, visited)
        path.pop()
        visited[row][col] = False

    def minimumEffortPath(self, heights) -> int:
        m, n = len(heights), len(heights[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        path, ans = [], []
        self.solve(heights, 0, 0, path, ans, visited)
        print(ans)


if __name__ == '__main__':
    heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    Solution().minimumEffortPath(heights)
