a, b = map(int, input().split())

def F(n):
    if n == 0:
        return 0
    res = n
    for i in range(1, 50):  # 2^50 > 10^15
        res += (n // (2**i)) * ((2**i - 2**(i - 1)))
    return res

print(F(b) - F(a - 1))