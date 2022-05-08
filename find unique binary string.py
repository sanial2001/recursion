class Solution:
    def solve(self, nums, res, cnt):
        if cnt >= self.n:
            if cnt == self.n and res not in self.visit:
                self.ans.append(res)
            return
        for val in nums:
            self.solve(nums, res + val, cnt + 1)

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        self.ans, self.n, self.visit = [], len(nums), nums
        self.solve(['0', '1'], '', 0)
        return self.ans[0]


class Solution:
    def solve(self, nums, res, cnt, n):
        if cnt >= n:
            if cnt == n and res not in self.visit:
                return res
            return 0
        for val in nums:
            temp = self.solve(nums, res + val, cnt + 1, n)
            if temp:
                return temp
            else:
                continue

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        self.visit = nums
        return self.solve(['0', '1'], '', 0, len(nums))
        # return self.ans[0]
