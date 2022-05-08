class Solution:
    def solve(self, n):
        if n == 0:
            return ['']
        elif n<0:
            return []
        one = self.solve(n-1)
        two = self.solve(n-2)
        res = []
        for i in range(len(one)):
            res.append('1'+one[i])
        for i in range(len(two)):
            res.append('2'+two[i])
        return res

    #Function to count number of ways to reach the nth stair.
    def countWays(self,n):
        return self.solve(n)


if __name__ == '__main__':
    print(Solution().countWays(4))
