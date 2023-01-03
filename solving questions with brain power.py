class Solution:
    def solve(self, questions, index):
        if index >= len(questions):
            return 0
        buy = self.solve(questions, index + 1 + questions[index][1]) + questions[index][0]
        skip = self.solve(questions, index + 1)
        return max(buy, skip)

    def mostPoints(self, questions: List[List[int]]) -> int:
        return self.solve(questions, 0)
