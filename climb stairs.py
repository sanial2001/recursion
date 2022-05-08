class Solution:
    def solve(self, n, nums, path, ans):
        if sum(path) >= n:
            if sum(path) == n:
                ans.append(path[:])
            return
        for i in range(len(nums)):
            path.append(nums[i])
            self.solve(n, nums, path, ans)
            path.pop()
        '''    
        path.append(1)
        self.solve(n, path, ans)
        path.pop()
        path.append(2)
        self.solve(n, path, ans)
        path.pop()
        '''

    def climbStairs(self, n):
        nums = [1, 2]
        path, ans = [], []
        self.solve(n, nums, path, ans)
        print(ans)
        print(len(ans))


if __name__ == '__main__':
    Solution().climbStairs(6)
