class Solution:
    def solve(self, arr, res, index, target, ans):
        if index == len(arr) or sum(res) > target:
            return
        elif sum(res) == target:
            ans.append(res[:])
            return
        res.append(arr[index])
        self.solve(arr, res, index, target, ans)
        res.remove(arr[index])
        self.solve(arr, res, index+1, target, ans)

    def combinationSum(self, candidates, target):
        res, ans = [], []
        self.solve(candidates, res, 0, target, ans)
        set_ans = set(tuple(ele) for ele in ans)
        print(set_ans)


class solution:
    def solve(self, nums, path, index, target, ans):
        if sum(path) >= target:
            if sum(path) == target:
                ans.append(path[:])
            return
        for i in range(index, len(nums)):
            path.append(nums[i])
            self.solve(nums, path, i, target, ans)
            path.pop()

    def combinationSum(self, candidates, target):
        res, ans = [], []
        self.solve(candidates, res, 0, target, ans)
        print(ans)


if __name__ == '__main__':
    arr = [7, 2, 6, 5]
    solution().combinationSum(arr, 16)
