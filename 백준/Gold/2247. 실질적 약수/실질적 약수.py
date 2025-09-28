def CSOD(n):
    ans = 0
    for i in range(2,n):
        ans += i * ((n//i)-1)
    return ans

n = int(input())
print(CSOD(n)%1000000)