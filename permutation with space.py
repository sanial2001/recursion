def solve(x, y):
    if len(x) == 0:
        print(y)
        return
    if len(y) == 0:
        solve(x[1:], y+x[0])
    else:
        solve(x[1:], y+' '+x[0])
        solve(x[1:], y+x[0])


if __name__ == '__main__':
    solve('abc', '')
