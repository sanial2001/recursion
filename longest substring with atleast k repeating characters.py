class Solution:
    def solve(self, s, k):
        if len(s) < k:
            return 0
        for i in set(s):
            if s.count(i) < k:
                split = s.split(i)
                ans = 0
                for substring in split:
                    ans = max(ans, self.solve(substring, k))
                return ans
        return len(s)

    def longestSubstring(self, s: str, k: int) -> int:
        return self.solve(s, k)
