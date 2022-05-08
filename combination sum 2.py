class Solution:
    def solve(self, nums, target, index, path, ans):
        if sum(path) >= target:
            if sum(path) == target:
                ans.append(path[:])
            return
        prev = -1
        for i in range(index, len(nums)):
            if nums[i] == prev:
                continue
            path.append(nums[i])
            self.solve(nums, target, i+1, path, ans)
            path.pop()
            prev = nums[i]

    def combinationSum2(self, candidates, target):
        res, ans = [], []
        candidates.sort()
        self.solve(candidates, target, 0, res, ans)
        print(ans)


if __name__ == '__main__':
    arr = [10,1,2,7,6,1,5]
    Solution().combinationSum2(arr, 7)
