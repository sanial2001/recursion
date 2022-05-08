def solve(nums, index):
    if index == len(nums)-1:
        return True
    return nums[index] < nums[index+1] and solve(nums, index+1)


if __name__ == '__main__':
    nums = [1, 3, 5, 8]
    print(solve(nums, 0))
