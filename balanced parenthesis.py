class solution:
    ans = []
    def solve(self, o, c, pattern):
        if o == 0 and c == 0:
            self.ans.append(pattern)
            return
        if o != 0:
            self.solve(o-1, c, pattern+'(')
        if c > o:
            self.solve(o, c-1, pattern+')')


    def balanced_parenthesis(self, n):
        self.solve(n, n, '')
        print(self.ans)


class Solution:
    ans = []

    def solve(self, o, c, pattern):
        if o == 0 and c == 0:
            self.ans.append(pattern)
        if o != 0:
            self.solve(o - 1, c, pattern + '(')
        if c > o:
            self.solve(o, c - 1, pattern + ')')

    def AllParenthesis(self, n):
        # code here
        self.solve(n, n, '')
        print(self.ans)


if __name__ == '__main__':
    Solution().AllParenthesis(3)
