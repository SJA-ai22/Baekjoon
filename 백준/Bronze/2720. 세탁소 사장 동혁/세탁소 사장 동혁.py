num = int(input())
result = []
q,d,n,p = 0,0,0,0
for i in range(num):
    data = int(input())
    record = []
    while data != 0:
            q = data // 25
            data -= q*25
            record.append(q)
            d = data // 10
            data -= d*10
            record.append(d)
            n = data // 5
            data -= n*5
            record.append(n)
            p = data // 1
            data -= p
            record.append(p)
    result.append(record)
for j in range(num):
    print(*result[j])