class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        A = list(A)
        n = len(A)
        for i in range(n):
            if A[i] == i + 1 or A[A[i] - 1] == A[i]:
                continue
            else:
                temp = A[i]
                A[i] = A[temp - 1]
                A[temp - 1] = temp
        print(A)
        return A[n - 1]


if __name__ == "__main__":
    Solution().repeatedNumber([3, 4, 1, 4, 1])
