import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
m = int(input())
data2 = list(map(int, input().split()))

data_freq = {}
for item in data:
    if item in data_freq:
        data_freq[item] += 1
    else:
        data_freq[item] = 1

result = []
for i in data2:
    if i in data_freq:
        result.append(data_freq[i])
    else:
        result.append(0)
print(*result)
