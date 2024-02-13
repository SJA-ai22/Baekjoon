n = int(input())
data = {}
for i in range(n):
    name, state = input().split()
    if state == 'enter':
        data[name] = True
    else:
        del data[name]

result = sorted(data.keys(), reverse = True)
for j in result:
    print(j)