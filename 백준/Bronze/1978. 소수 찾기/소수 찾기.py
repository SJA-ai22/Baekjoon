num = int(input())
data = list(map(int,input().split()))
result = 0
for i in range(num):
    if data[i] == 2:
        result += 1
    else:
        b = int(data[i]/2)+1
        for j in range(2,b+1):
            if data[i] % j == 0:
                break
            elif j == b:
                result += 1
print(result)