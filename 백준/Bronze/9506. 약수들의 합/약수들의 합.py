data = []
num = 0
while True:
    try:
        a = int(input())
    except ValueError:
        break
    if a == -1:
        break
    num += 1
    b = []
    b.append(a)
    b.append('=')
    result = 0
    for i in range(1,a):
        if a % i == 0:
            b.append(i)
            result += i
            b.append('+')
    b.pop()
    if a == result:
        data.append(b)
    else:
        c = []
        c.append(a)
        c.append('is NOT perfect.')
        data.append(c)
for k in range(num):
    print(*data[k])