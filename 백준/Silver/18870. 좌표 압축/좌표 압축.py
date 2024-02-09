N = int(input())
data = list(map(int, input().split()))
SortData = sorted(list(set(data)))
dic = {}

for i in range(len(SortData)):
  dic[SortData[i]] = i

for i in data:
  print(dic[i], end=" ")