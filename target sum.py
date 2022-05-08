def solve(arr, target, n):
    if len(arr) == 0:
        return 0
    if target == 0:
        return 1
    if arr[n-1] <= target:
        return 


if __name__ == '__main__':
    arr = [10, 20, 30, 40, 50, 60]
    s = 60
    solve(arr, 0, s, 0, '')
