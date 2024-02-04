num = int(input())
data = []
result = ''
for i in range(num):
    a = list(map(int, input().split()))
    a.reverse()
    data.append(a)
data.sort()
for j in data:
    j.reverse()
    print(j[0], j[1])