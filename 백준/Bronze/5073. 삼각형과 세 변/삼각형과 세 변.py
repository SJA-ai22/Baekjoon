data = []
count = 0
while(True):
    a,b,c = map(int, input().split())
    if a==b==c==0:
        break
    else:
        if max(a,b,c) >= ((a+b+c)-max(a,b,c)):
            data.append('Invalid')
        else:
            if a==b==c:
                data.append('Equilateral')
            elif a == b or b == c or a == c:
                data.append('Isosceles')
            else:
                data.append('Scalene')
        count += 1
for i in range(count):
    print(data[i])