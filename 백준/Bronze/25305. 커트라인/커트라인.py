n, k = map(int, input().split())
data = list(map(int,input().split()))
result = []
while data != []:
    max = data[0]
    for j in range(len(data)):
        if data[j] > max:
            max = data[j]
    data.remove(max)
    result.append(max)
print(result[k-1])