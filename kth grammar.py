def solve(n, k):
    val = [0]
    val2 = [0]
    for i in range(1, n):
        val = []
        mid = pow(2, i) // 2
        for j in range(pow(2, i)):
            if j < mid:
                val.append(val2[j])
            else:
                temp = 0
                if val2[j-mid] == 0:
                    temp = 1
                val.append(temp)
        val2 = val
    return val[k-1]


def solve_rec(n, k):
    if n == 0 and k == 0:
        return 0
    mid = pow(2, n-1) // 2
    if k <= mid:
        return solve_rec(n-1, k)
    else:
        return not solve_rec(n-1, k-mid)


if __name__ == '__main__':
    print(solve_rec(4, 5))
