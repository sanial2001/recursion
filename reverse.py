def solve(num):
    if len(num) == 1:
        return num
    x = num[0]
    res = solve(num[1:])
    ans = res + x
    return ans


if __name__ == '__main__':
    print(solve('49243'))
