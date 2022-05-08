def xor(arr):
    val = arr[0]
    for i in arr[1:]:
        val = val ^ i
    return val


def xor_cal(arr, n):
    subsegment = []
    for i in range(n):
        for j in range(i, n):
            subsegment.append(arr[i:j+1])

    xor_sum = 0
    for val in subsegment:
        xor_sum = xor_sum + xor(val)
    return xor_sum


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        a = input().split()
        a = [int(i, 16) for i in a]
        print(xor_cal(a, n))
