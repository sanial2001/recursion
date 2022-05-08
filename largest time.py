class Solution:
    def valid(self, time):
        if time[0] > 2 or time[0] < 0:
            return False
        if time[0] == 2 and time[1] > 3:
            return False
        if time[2] > 5 or time[0] < 0:
            return False
        return True

    def solve(self, arr):
        if len(arr) == 1:
            return [arr]
        res = []
        for i in range(len(arr)):
            val = arr[i]
            rem = self.solve(arr[:i] + arr[i + 1:])
            for j in range(len(rem)):
                temp = [val] + rem[j]
                if len(temp) == 4:
                    if self.valid(temp):
                        res.append([val] + rem[j])
                else:
                    res.append([val] + rem[j])
        return res

    def largestTimeFromDigits(self, arr: List[int]) -> str:
        res = self.solve(arr)
        if not res:
            return ""
        res.sort()
        ans = res.pop()
        ans = [str(i) for i in ans]
        ans.insert(2, ":")
        return "".join(ans)
