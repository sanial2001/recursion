class Solution:
    def __init__(self):
        self.mob = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    def letterCombinations(self, digits):
        if len(digits) == 0:
            return ['']
        num = digits[0]
        rem = self.letterCombinations(digits[1:])
        match = self.mob[int(num)]
        ans = []
        for i in range(len(match)):
            char = match[i]
            for j in range(len(rem)):
                x = char + rem[j]
                ans.append(x)
        return ans


if __name__ == '__main__':
    print(Solution().letterCombinations('23'))