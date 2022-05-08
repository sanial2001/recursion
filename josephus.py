def solve(arr, k, index):
    if len(arr) == 1:
        return arr
    k = 6
    index = (index + k) % len(arr)
    arr.pop(index)
    print(len(arr))
    solve(arr, k, index)


def josephus(n, k):
    arr = [(i+1) for i in range(n)]
    index = 0
    return solve(arr, k, index)


if __name__ == '__main__':
    n, k = 40, 7
    print(josephus(n, k))
