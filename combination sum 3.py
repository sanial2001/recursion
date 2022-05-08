class Solution:
    def solve(self, nums, index, k, target, path, ans):
        if sum(path) > target:
            return
        if sum(path) == target and len(path) == k:
            ans.append(path[:])
            return
        for i in range(index, len(nums)):
            path.append(nums[i])
            self.solve(nums, i+1, k, target, path, ans)
            path.pop()

    def combinationSum3(self, k: int, n: int):
        nums = [i+1 for i in range(9)]
        path, ans = [], []
        self.solve(nums, 0, k, n, path, ans)
        print(ans)


if __name__ == '__main__':
    Solution().combinationSum3(3, 7)
