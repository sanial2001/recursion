def solve(ones, zeros, n, output):
    if n == 0:
        print(output)
        return
    solve(ones+1, zeros, n-1, output+'1')
    if ones > zeros:
        solve(ones, zeros+1, n-1, output+'0')


def n_bit_binary(n):
    solve(0, 0, n, '')


if __name__ == '__main__':
    n_bit_binary(3)
