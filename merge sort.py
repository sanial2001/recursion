def merge(left, right):
    i, j = 0, 0
    m, n = len(left), len(right)
    res = []
    while i<m and j<n:
        if left[i] < right[j]:
            res.append(left[i])
            i = i+1
        else:
            res.append(right[j])
            j = j+1

    while i<m:
        res.append(left[i])
        i = i+1

    while j<n:
        res.append(right[j])
        j = j+1

    return res


def solve(nums):
    if len(nums) == 1:
        return nums
    start, end = 0, len(nums)-1
    mid = (start + end) // 2
    left = solve(nums[start:mid+1])
    right = solve(nums[mid+1:end+1])
    return merge(left, right)


if __name__ == '__main__':
    arr = [8, 3, 4, 12, 5, 6]
    print(solve(arr))