class Solution:
	def __init__(self):
		self.pos = []

	def knight_tour(self, row, col, n, board):
		if row < 0 or col < 0 or row >= n or col >= n or board[row][col] == 1:
			return
		elif len(self.pos) == n**2:
			return
		board[row][col] = 1
		self.pos.append([row + 1, col + 1])
		self.knight_tour(row - 2, col + 1, n, board)
		self.knight_tour(row - 1, col + 2, n, board)
		self.knight_tour(row + 1, col + 2, n, board)
		self.knight_tour(row + 2, col + 1, n, board)
		self.knight_tour(row + 2, col - 1, n, board)
		self.knight_tour(row + 1, col - 2, n, board)
		self.knight_tour(row - 1, col - 2, n, board)
		self.knight_tour(row - 2, col - 1, n, board)
		board[row][col] = 0

	def moves(self, r, c, n):
		board = [[0 for _ in range(n)] for _ in range(n)]
		self.knight_tour(r-1, c-1, n, board)
		for i, val in enumerate(self.pos):
			print('{0} move : {1}'.format(i+1, val))


if __name__ == '__main__':
	Solution().moves(3, 3, 8)
