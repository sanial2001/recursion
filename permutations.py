class Solution:
    def solve(self, nums):
        if len(nums) <= 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            new_nums = nums[:i] + nums[i+1:]
            rem = self.solve(new_nums)
            for j in range(len(rem)):
                temp = rem[j] + [nums[i]]
                res.append(temp)
        return res

    def permute(self, nums):
        print(self.solve(nums))


if __name__ == '__main__':
    arr = ['a', 'b', 'c']
    Solution().permute(arr)
