class Solution:
    def solve(self, num, path, n):
        if num > n:
            return
        if len(path) == n:
            return
        path.append(num)
        print(path)
        for i in range(10):
            self.solve(num*10 + i, path, n)

    def lexicalOrder(self, n: int):
        path = []
        for i in range(1, n+1):
            self.solve(i, path, n)
        print(path)


if __name__ == '__main__':
    Solution().lexicalOrder(57)