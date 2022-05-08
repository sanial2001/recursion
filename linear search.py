def solve(nums, index, target):
    if index == len(nums)-1:
        return False
    return nums[index] == target or solve(nums, index+1, target)


if __name__ == '__main__':
    nums = [1, 5, 6, 4, 3]
    print(solve(nums, 0, 2))
