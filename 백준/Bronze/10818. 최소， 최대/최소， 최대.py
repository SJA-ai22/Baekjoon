num = int(input())
data = list(map(int, input().split()))
min = data[0]
max = data[0]

for i in range(num):
  if(min > data[i]):
    min = data[i]
  if(max < data[i]):
    max = data[i]

print(min, max)