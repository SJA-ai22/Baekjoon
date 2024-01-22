n, m = map(int,input().split())
data = list(map(int, input().split()))
result = 0
ex = []
for i in range(len(data)):
    for j in range(i+1,len(data)):
        for k in range(j+1,len(data)):
            jack = data[i] + data[j] + data[k]
            if result < jack and jack <= m:
                result = jack
print(result)