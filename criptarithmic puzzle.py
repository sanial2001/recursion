class Solution:
    def solve(self, char_map, words, result, index, visited):
        if index >= len(char_map):
            x1, x2, x3 = '', '', ''
            for ch in words[0]:
                x1 = x1 + char_map[ch]
            for ch in words[1]:
                x2 = x2 + char_map[ch]
            for ch in result:
                x3 = x3 + char_map[ch]
            x1 = int(x1)
            x2 = int(x2)
            x3 = int(x3)
            if x1 + x2 == x3:
                print(x1, x2, x3)
                self.ans = True
            return

        ch = char_map[list(char_map)[index]]
        for i in range(10):
            if visited[i] == False:
                char_map[ch] = i
                visited[i] = True
                self.solve(char_map, words, result, index+1, visited)
                visited[i] = False
                char_map[i] = -1

    def isSolvable(self, words, result: str) -> bool:
        char_map = {}
        self.ans = False
        visited = [False for _ in range(10)]
        for word in words:
            for ch in word:
                if ch not in char_map:
                    char_map[ch] = -1

        for ch in result:
            if ch not in char_map:
                char_map[ch] = -1

        self.solve(char_map, words, result, 0, visited)
        return self.ans


if __name__ == '__main__':
    print(Solution().isSolvable(['SEND', 'MORE'], 'MONEY'))
