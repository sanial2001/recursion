class Solution:
    def solve(self, nums, index, target, path):
        if sum(path) >= target:
            if sum(path) == target:
                print(path)
                self.cnt += 1
                print(self.cnt)
            return
        for i in range(len(nums)):
            path.append(nums[i])
            self.solve(nums, i, target, path)
            path.pop()

    def combinationSum4(self, nums, target) -> int:
        path, self.cnt = [], 0
        self.solve(nums, 0, target, path)
        print(self.cnt)


if __name__ == '__main__':
    arr = [1, 2, 3]
    Solution().combinationSum4(arr, 4)