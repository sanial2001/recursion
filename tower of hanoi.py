class Solution:
    def __init__(self):
        self.cnt = 0

    def solve(self, n, a, b, c):
        if n == 0:
            return
        self.solve(n - 1, a, b, c)
        self.cnt += 1
        print('move disk {0} from rod {1} to rod {2}'.format(n, a, b))
        self.solve(n - 1, c, b, a)

    def toh(self, N, fromm, to, aux):
        # Your code here
        self.solve(N, fromm, to, aux)
        print(self.cnt)


if __name__ == "__main__":
    Solution().toh(3, 'a', 'b', 'c')