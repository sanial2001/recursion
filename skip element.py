def solve(str, index, ans):
    if index == len(str):
        return
    if str[index] != 'a':
        ans.append(str[index])
    solve(str, index+1, ans)


def skip(str):
    ans = []
    solve(str, 0, ans)
    return ''.join(ans)


if __name__ == '__main__':
    print(skip('cabbad'))
