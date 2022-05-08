class Solution:
    def solve(self, word):
        if len(word) <= 1:
            return word
        res = []
        prev = ''
        for i in range(len(word)):
            if prev == word[i]:
                continue
            new_word = word[:i] + word[i+1:]
            rem = self.solve(new_word)
            for j in range(len(rem)):
                temp = rem[j] + word[i]
                res.append(temp)
            prev = word[i]
        return res

    def permute(self, word):
        print(self.solve(word))


if __name__ == '__main__':
    word = 'aabb'
    word = sorted(word)
    Solution().permute(word)
