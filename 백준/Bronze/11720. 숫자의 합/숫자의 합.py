num = int(input())
data = list(map(int,input()))
result = 0

for i in range(num):
    result += data[i]
print(result)