result = []
a,b = map(int, input().split())
while a != 0 and b != 0:
    if b % a == 0:
        result.append('factor')
    elif a % b == 0:
        result.append('multiple')
    else:
        result.append('neither')
    a,b = map(int, input().split())
for i in range(len(result)):
    print(result[i])