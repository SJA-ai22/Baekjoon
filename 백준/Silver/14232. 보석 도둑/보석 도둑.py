n = int(input())
ans = []

num = 2
while num <= (n**0.5):
    while n % num == 0:
        ans.append(num)
        n //= num
    num += 1

if n > 1:
    ans.append(n)

print(len(ans))
print(*ans)   