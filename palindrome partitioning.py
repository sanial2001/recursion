class Solution:
    def solve(self, s, index, path, ans):
        if index == len(s):
            ans.append(path[::])
            return
        for i in range(index, len(s)):
            if s[index:i + 1] == s[index:i + 1][::-1]:
                path.append(s[index:i + 1])
                self.solve(s, i + 1, path, ans)
                path.pop()

    def partition(self, s: str):
        path, ans = [], []
        self.solve(s, 0, path, ans)
        return ans
