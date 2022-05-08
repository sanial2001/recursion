class Solution:
    def solve(self, word):
        if len(word) <= 1:
            return word
        res = []
        for i in range(len(word)):
            new_word = word[:i] + word[i+1:]
            rem = self.solve(new_word)
            for j in range(len(rem)):
                temp = rem[j] + word[i]
                res.append(temp)
        return res

    def permute(self, word):
        print(self.solve(word))


if __name__ == '__main__':
    word = 'abc'
    Solution().permute(word)
