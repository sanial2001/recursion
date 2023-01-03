def solve(N, n, prev):
    print(n)
    if n <= 0:
        return 0
    res = float("inf")
    res = min(res, solve(N, n - 1, prev) + 1, solve(N, n - prev, prev) + 2, solve(N, n, N - n) + 4)
    return res


if __name__ == "__main__":
    N = int(input())
    print(solve(N, N, 1))
