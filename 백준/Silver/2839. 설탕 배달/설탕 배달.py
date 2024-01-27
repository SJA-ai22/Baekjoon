n = int(input())
a = int(n / 5)
b = 0
while a >= 0:
    if a*5 + b*3 == n:
        print(a+b)
        break
    elif a*5 + b*3 < n:
        b += 1
    else:
        b = 1
        a -= 1
if a == -1:
    print(-1)