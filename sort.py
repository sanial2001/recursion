class Solution:
    def __init__(self):
        self.x = [4, 6, 2, 1]
        self.sort()
        print(self.x)

    def sort(self):
        if len(self.x) == 1:
            return
        temp = self.x.pop()
        self.sort()
        self.insert(temp)

    def insert(self, temp):
        if len(self.x) == 0 or temp >= self.x[len(self.x) - 1]:
            self.x.append(temp)
            return
        temp2 = self.x.pop()
        self.insert(temp)
        self.x.append(temp2)


if __name__ == '__main__':
    Solution()
