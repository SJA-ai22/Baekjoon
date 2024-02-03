num = int(input())
data = []
result = ''
for i in range(num):
    data.append(list(map(int, input().split())))
data.sort()
for j in data:
    print(j[0], j[1])