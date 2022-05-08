class Solution:
    def __init__(self):
        self.mobile = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    def solve(self, a):
        if len(a) == 0:
            blank = ['']
            return blank
        ch = a[0]
        rem = self.solve(a[1:])
        res = []
        match = self.mobile[ch]
        for i in range(len(match)):
            ch_match = match[i]
            for j in range(len(rem)):
                res.append(ch_match+rem[j])
        return res

    # Function to find list of all words possible by pressing given numbers.
    def possibleWords(self, a, N):
        return self.solve(a)


if __name__ == '__main__':
    a = [2, 3, 4]
    print(Solution().possibleWords(a, len(a)))
