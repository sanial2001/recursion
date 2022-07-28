class Solution:
    def solve(self, k):
        if k < 2:
            return k
        n1, n2 = 1, 1
        while n2 <= k:
            n2, n1 = n1 + n2, n2
        return self.solve(k - n1) + 1

    def findMinFibonacciNumbers(self, k: int) -> int:
        return self.solve(k)
