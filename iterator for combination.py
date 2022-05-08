class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.res = []

        def solve(word, index, path):
            if len(path) >= combinationLength:
                if len(path) == combinationLength:
                    self.res.append(path)
                return
            for i in range(index, len(word)):
                solve(word, i + 1, path + word[i])

        solve(characters, 0, '')
        # print(self.res)

    def next(self) -> str:
        return self.res.pop(0)

    def hasNext(self) -> bool:
        return True if self.res else False

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
