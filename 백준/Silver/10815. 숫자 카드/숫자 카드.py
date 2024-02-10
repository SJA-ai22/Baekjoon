n = int(input())
card = set(map(int, input().split()))
m = int(input())
data = list(map(int, input().split()))
result = [0]*m

for i in range(m):
    if data[i] in card:
        result[i] = 1
    else:
        result[i] = 0
print(*result)