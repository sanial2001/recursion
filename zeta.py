class Solution:
    def make_dict(self, word):
        d = {}
        for i in word:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1
        return d

    def wordSubsets(self, words1, words2):
        res = []
        for word2 in words2:
            for char in word2:
                if char.count()
        w2 = ''.join(words2)
        dict2 = self.make_dict(w2)
        print(dict2)

        for word1 in words1:
            dict1 = self.make_dict(word1)
            temp = 0
            for key in dict2:
                if key in dict1 and dict2[key] >= dict1[key]:
                    temp += 1
                else:
                    break
            if temp == len(dict2):
                res.append(word1)

        print(res)


if __name__ == "__main__":
    words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
    words2 = ["lo", "eo"]
    Solution().wordSubsets(words1, words2)


