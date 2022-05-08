class Solution:
    def solve(self, nums, index, curr, path):
        if index > len(nums):
            return
        if len(path) >= 2:
            self.ans.append(path)
        for i in range(index, len(nums)):
            if nums[i] >= curr:
                self.solve(nums, i + 1, nums[i], path + [nums[i]])

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.solve(nums, 0, -float("inf"), [])
        res = []
        for val in self.ans:
            if val not in res:
                res.append(val)
        return res


class Solution:
    def solve(self, nums, index, curr, path):
        if index > len(nums):
            return
        if len(path) >= 2:
            self.ans.add(path)
        for i in range(index, len(nums)):
            if nums[i] >= curr:
                self.solve(nums, i + 1, nums[i], path + (nums[i],))

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.ans = set()
        self.solve(nums, 0, -float("inf"), ())
        return self.ans
