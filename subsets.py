class Solution:
    def solve(self, nums, index, path, ans):
        ans.append(path[:])
        for i in range(index, len(nums)):
            path.append(nums[i])
            self.solve(nums, i+1, path, ans)
            path.pop()
        '''    
        self.solve(nums[1:], path, ans)
        x = nums[0]
        path.append(x)
        self.solve(nums[1:], path, ans)
        path.pop()
        '''

    def subsets(self, nums):
        path, ans = [], []
        self.solve(nums, 0, path, ans)
        print(ans)


if __name__ == '__main__':
    arr = [1, 2, 3]
    Solution().subsets(arr)
