class Solution:
    def dfs(self, num, n, k):
        if n == 0:
            # print(num)
            self.ans.append(int(num))
            return
        else:
            digit = num[-1]
            if int(digit) - k >= 0:
                self.dfs(num + str(int(digit) - k), n - 1, k)
            if int(digit) + k < 10:
                self.dfs(num + str(int(digit) + k), n - 1, k)

    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if k == 0:
            return [int(str(i) * n) for i in range(1, 10)]
        self.ans = []
        for i in range(1, 10):
            self.dfs(str(i), n - 1, k)
        return self.ans
