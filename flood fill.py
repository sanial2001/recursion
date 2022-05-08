class Solution:
    def solve(self, image, row, col, nc, oc):
        if row < 0 or col < 0 or row == len(image) or col == len(image[0]) or image[row][col] != oc:
            return
        image[row][col] = nc
        self.solve(image, row - 1, col, nc, oc)
        self.solve(image, row, col - 1, nc, oc)
        self.solve(image, row + 1, col, nc, oc)
        self.solve(image, row, col + 1, nc, oc)

    def floodFill(self, image, sr: int, sc: int, newColor: int):
        self.solve(image, sr, sc, newColor, image[sr][sc])
        for val in image:
            print(val)


if __name__ == '__main__':
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    Solution().floodFill(image, 1, 1, 2)
