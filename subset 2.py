class Solution:
    def solve(self, nums, index, path, ans):
        ans.append(path[:])
        prev = -10000
        for i in range(index, len(nums)):
            if prev == nums[i]:
                continue
            path.append(nums[i])
            self.solve(nums, i + 1, path, ans)
            path.pop()
            prev = nums[i]

    def subsetsWithDup(self, nums):
        path, ans = [], []
        nums.sort()
        self.solve(nums, 0, path, ans)
        print(ans)


if __name__ == '__main__':
    arr = [4, 4, 4, 1, 4]
    Solution().subsetsWithDup(arr)
