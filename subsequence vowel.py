class Solution:
    def __init__(self):
        self.result = []

    def check(self, s):
        vow = ['a', 'e', 'i', 'o', 'u']
        if s in vow:
            return True
        else:
            return False

    def solve(self, x, y):
        if len(x) == 0:
            if len(y) > 0 and self.check(y[0]) == True and self.check(y[-1]) == False:
                self.result.append(y)
            return
        self.solve(x[1:], y + x[0])
        self.solve(x[1:], y)

    def allPossibleSubsequences(self, S):
        self.solve(S, '')
        self.result.sort()
        return self.result


class solution:
    def check(self, s):
        vow = ['a', 'e', 'i', 'o', 'u']
        if s in vow:
            return True
        else:
            return False

    def solve(self, S):
        if len(S) == 0:
            blank = ['']
            return blank
        ch = S[0]
        rem = self.solve(S[1:])
        res = []
        for i in range(len(rem)):
            res.append(ch + rem[i])
            res.append('' + rem[i])
        return res

    def allPossibleSubsequences(self, S):
        res = self.solve(S)
        ans = []
        for i in range(len(res)):
            if len(res[i]) > 0 and self.check(res[i][0]) == True and self.check(res[i][-1]) == False:
                ans.append(res[i])
        return ans


if __name__ == '__main__':
    print(solution().allPossibleSubsequences('abc'))
