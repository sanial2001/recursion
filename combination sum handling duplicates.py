class Solution:
    def DFS(self, candidates, target, start, res, intermedia):
        if target == 0:
            res.append(intermedia)
            return
        for i in range(start, len(candidates)):
            if target < candidates[i]:
                return
            self.DFS(candidates, target - candidates[i], i, res, intermedia + [candidates[i]])

    # Function to return a list of indexes denoting the required
    # combinations whose sum is equal to given number.
    def combinationalSum(self, A, B):
        A.sort()
        res = []
        self.DFS(A, B, 0, res, [])
        set_ans = set(tuple(ele) for ele in res)
        res = list(set_ans)
        print(res)


if __name__ == '__main__':
    arr = [8, 1, 8, 6, 8]
    Solution().combinationalSum(arr, 12)