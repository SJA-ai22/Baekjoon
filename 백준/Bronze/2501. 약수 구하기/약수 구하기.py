num, a = map(int, input().split())
data = []
for i in range(1,num+1):
    if num % i == 0:
        data.append(i)
if a > len(data):
    print(0)
else:
    print(data[a-1])