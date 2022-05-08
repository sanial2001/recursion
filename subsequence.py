def solve(x, y):
    if len(x) == 0:
        print(y)
        return
    solve(x[1:], x[0]+y)      # element taken
    solve(x[1:], y)           # element not taken


def Solve(x):
    if len(x) == 0:
        return ['']
    item = x[0]
    res = Solve(x[1:])
    ans = []
    for i in res:
        ans.append(i+item)
        ans.append(i)
    return ans


if __name__ == "__main__":
    solve('abc', '')
    print(Solve('abc'))
