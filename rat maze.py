class Solution:
    def solve(self, maze, row, col, path, visited):
        if row < 0 or col < 0 or row >= len(maze) or col >= len(maze[0]) or maze[row][col] == 0 or visited[row][col] == True:
            return
        elif row == len(maze) - 1 and col == len(maze) - 1:
            print(path)
            return
        visited[row][col] = True
        self.solve(maze, row - 1, col, path + 'T', visited)
        self.solve(maze, row, col - 1, path + 'L', visited)
        self.solve(maze, row + 1, col, path + 'D', visited)
        self.solve(maze, row, col + 1, path + 'R', visited)
        visited[row][col] = False

    def findPath(self, m, n):
        visited = [[False for _ in range(n)] for _ in range(n)]
        self.solve(m, 0, 0, '', visited)


if __name__ == '__main__':
    m = [[1, 0, 0, 0],
         [1, 1, 0, 1],
         [1, 1, 0, 0],
         [0, 1, 1, 1]]
    n = 4
    Solution().findPath(m, n)
