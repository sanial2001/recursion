def solve(n):
    if n // 10 == 0:
        return n
    x = solve(n // 10)
    return x * (n % 10)


if __name__ == '__main__':
    print(solve(1342))
