num = int(input())
data = [[],[]]
result = 0
for i in range(num):
    a,b = map(int, input().split())
    data[0].append(a)
    data[1].append(b)
j = max(data[0]) - min(data[0])
k = max(data[1]) - min(data[1])
result = j * k
print(result)
