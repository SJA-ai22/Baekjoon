n = int(input())
data = []
for i in range(n):
    a,b = input().split()
    a = int(a)
    c = [a,b]
    data.append(c)
data.sort(key=lambda x : x[0])
for j in data:
    print(*j)