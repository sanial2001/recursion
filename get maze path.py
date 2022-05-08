class Solution:
    def solve(self, r, c, m, n):
        if r == m and c == n:
            return ['']
        hpath, vpath = [], []
        if r < m:
            vpath = self.solve(r+1, c, m, n)
        if c < n:
            hpath = self.solve(r, c+1, m, n)
        res = []
        for i in range(len(hpath)):
            res.append('h'+hpath[i])
        for i in range(len(vpath)):
            res.append('v'+vpath[i])
        return res

    def uniquepath(self, m, n):
        res = self.solve(1, 1, m, n)
        return len(res)


if __name__ == '__main__':
    print(Solution().uniquepath(6, 6))
