def solve(x, y):
    if len(x) == 0:
        print(y)
        return
    if x[0].isdigit():
        solve(x[1:], y+x[0])
    else:
        solve(x[1:], y+x[0].lower())
        solve(x[1:], y+x[0].upper())


if __name__ == '__main__':
    solve('a1c2', '')
